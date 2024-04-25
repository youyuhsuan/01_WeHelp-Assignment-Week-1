from fastapi import FastAPI, Request, HTTPException, status, Header, Form, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from starlette.middleware.sessions import SessionMiddleware
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="templates")


class User(BaseModel):
    username: str
    disabled: bool | None = None


fake_users_db = {
    "test": {
        "username": "test",
        "password": "test",
        "disabled": False,
    }
}


@app.get("/", response_class=HTMLResponse)
async def root(
    request: Request,
):
    return templates.TemplateResponse("home.html", {"request": request})


@app.post("/signin", response_model=User)
async def signin(
    request: Request,
    username: str = Form(None, description="Username"),
    password: str = Form(None, description="Password"),
):
    if not username or not password:
        raise HTTPException(
            status_code=422, detail="Username or password cannot be empty"
        )
    user_data = fake_users_db.get(username)
    if user_data is None or user_data["password"] != password:
        raise HTTPException(
            status_code=401, detail="Username or password is not correct"
        )
    request.session["SIGNED-IN"] = True
    return RedirectResponse(url="/member", status_code=status.HTTP_303_SEE_OTHER)


async def http_exception_handler(request: Request, exc: HTTPException):
    if exc.status_code == 401 or exc.status_code == 422:
        error_message = "Username or password is not correct"
        return RedirectResponse(
            url=f"/error?message={error_message}", status_code=status.HTTP_303_SEE_OTHER
        )
    elif exc.status_code == 403:
        error_message = "Please log in to access this resource"
        return RedirectResponse(url="/", status_code=status.HTTP_307_TEMPORARY_REDIRECT)


app.add_exception_handler(HTTPException, http_exception_handler)


@app.get("/error")
async def error(request: Request, message: str = None):
    return templates.TemplateResponse("error.html", {"request": request})


@app.get("/member")
async def member(request: Request):
    SIGNED_IN = request.session.get("SIGNED-IN")
    if not SIGNED_IN:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    return templates.TemplateResponse("member.html", {"request": request})


@app.get("/signout")
async def signout(request: Request):
    request.session["SIGNED-IN"] = False
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

if __name__ == "__main__":
    uvicorn.run(app="main:app", host="127.0.0.1", port=8000, reload=True)
