from fastapi import FastAPI, Request, Response, HTTPException, status, Form, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.encoders import jsonable_encoder
from fastapi.templating import Jinja2Templates
from typing import Annotated
from starlette.middleware.sessions import SessionMiddleware
from passlib.context import CryptContext
from pydantic import BaseModel
import mysql.connector
from mysql.connector import errorcode
import uvicorn
import json


def get_db():
    try:
        cnx = mysql.connector.connect(
            user="root",
            password="cjfidjfisdjciosdj",
            host="localhost",
            database="website",
        )
        print("Connect success")
        cursor = cnx.cursor(buffered=True)
        yield cnx, cursor

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
            raise HTTPException(status_code=401, detail="Invalid credentials")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
            raise HTTPException(status_code=404, detail="Database not found")
        else:
            print(f"Database connection error: {err}")
            raise HTTPException(status_code=500, detail="Database connection error")
    finally:
        cnx.close()


class SessionData(BaseModel):
    name: str
    username: str
    message_id: int
    scopes: list[str] = []


class UserBase(BaseModel):
    username: str
    disabled: bool | None = None


class UserCreate(UserBase):
    name: str
    hashed_password: str


app = FastAPI()
templates = Jinja2Templates(directory="templates")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


@app.get("/", response_class=HTMLResponse)
async def root(
    request: Request,
):
    return templates.TemplateResponse("home.html", {"request": request})


@app.post("/signup", response_model=UserCreate)
async def signin(
    request: Request,
    name: Annotated[str, Form(description="Name")],
    username: Annotated[str, Form(description="Username")],
    password: Annotated[str, Form(description="Password")],
    db: tuple = Depends(get_db),
):
    cnx, cursor = db
    hashed_password = get_password_hash(password)
    query = "SELECT username FROM member WHERE username = %s"
    cursor.execute(query, (username,))
    matched_user = cursor.fetchone()
    if matched_user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Repeated username",
        )
    else:
        user_data = UserCreate(
            name=name, username=username, hashed_password=hashed_password
        )
        insert_new_account = (
            "INSERT INTO member (name, username, hashed_password) VALUES (%s, %s, %s)"
        )
        cursor.execute(
            insert_new_account,
            (user_data.name, user_data.username, user_data.hashed_password),
        )
        cnx.commit()
        return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)


@app.post("/signin", response_model=UserBase)
async def signin(
    request: Request,
    username: Annotated[str, Form(description="Username")],
    password: Annotated[str, Form(description="Password")],
    db: tuple = Depends(get_db),
):
    cnx, cursor = db  # 从db中提取cnx和cursor
    print(db)
    matched_user = UserBase(username=username)
    query = "SELECT id,name, username, hashed_password FROM member WHERE username = %s"
    cursor.execute(query, (matched_user.username,))
    matched_user = cursor.fetchone()
    if not matched_user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Username or password is not correct",
        )
    if not verify_password(password, matched_user[3]):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid password",
        )

    request.session["SIGNED_IN"] = matched_user[2]
    request.session["MEMBER_ID"] = matched_user[0]
    request.session["PAGE_NAME"] = matched_user[1]
    return RedirectResponse(url="/member", status_code=status.HTTP_303_SEE_OTHER)


async def http_exception_handler(request: Request, exc: HTTPException):
    if exc.status_code == 403 or exc.status_code == 422:
        error_message = exc.detail
        return RedirectResponse(
            url=f"/error?message={error_message}", status_code=status.HTTP_303_SEE_OTHER
        )


app.add_exception_handler(HTTPException, http_exception_handler)


@app.get("/error")
async def error(
    request: Request,
    message: str = None,
):
    return templates.TemplateResponse(
        "error.html",
        {"request": request, "error_message": message},
    )


@app.get("/member")
async def member(
    request: Request,
    db: tuple = Depends(get_db),
):
    cursor = db
    SIGNED_IN = request.session.get("SIGNED_IN")
    MEMBER_ID = request.session.get("MEMBER_ID")
    PAGE_NAME = request.session.get("PAGE_NAME")
    if not SIGNED_IN:
        return RedirectResponse(url="/", status_code=status.HTTP_307_TEMPORARY_REDIRECT)
    query = "SELECT message.id ,message.member_id ,member.name ,message.content FROM message JOIN member ON member.id = message.member_id ORDER BY message.time"
    cursor.execute(query)
    messages = cursor.fetchall()
    return templates.TemplateResponse(
        "member.html",
        {
            "request": request,
            "PAGE_NAME": PAGE_NAME,
            "MEMBER_ID": MEMBER_ID,
            "messages": messages,
        },
    )


@app.delete("/deleteMessage/{messageId}")
async def deleteMessage(
    request: Request,
    messageId: int,
    db: tuple = Depends(get_db),
):
    cnx, cursor = db
    query = "SELECT member.id FROM message JOIN member ON member.id = message.member_id WHERE message.id= %s"
    cursor.execute(query, (messageId,))
    matched_message = cursor.fetchone()
    if matched_message:
        delete_message = "DELETE FROM message WHERE message.id = %s"
        cursor.execute(delete_message, (messageId,))
        cnx.commit()
        return Response(
            content=json.dumps({"message": "Item deleted successfully"}),
            media_type="application/json",
        )
    else:
        return Response(
            content=json.dumps({"message": "Item not found"}),
            status_code=404,
            media_type="application/json",
        )


@app.post("/createMessage")
async def createMessage(
    request: Request,
    content: Annotated[str, Form(description="Content")],
    db: tuple = Depends(get_db),
):
    cnx, cursor = db
    MEMBER_ID = request.session.get("MEMBER_ID")
    insert_new_message = "INSERT INTO message(member_id,content) VALUES (%s,%s)"
    cursor.execute(insert_new_message, (MEMBER_ID, content))
    cnx.commit()
    return RedirectResponse(url="/member", status_code=status.HTTP_303_SEE_OTHER)


@app.get("/signout")
async def signout(request: Request):
    request.session.clear()
    return RedirectResponse(url="/", status_code=status.HTTP_307_TEMPORARY_REDIRECT)


@app.get("/square/{number}")
async def square_number(request: Request, number: int = 0):
    squared_number = number * number
    return templates.TemplateResponse(
        "square.html", {"request": request, "squared_number": squared_number}
    )


app.add_middleware(
    SessionMiddleware,
    secret_key="some-random-string",
    max_age=None,
    session_cookie="session",
)

app.mount("/static", StaticFiles(directory="static"), name="static")
