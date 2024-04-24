from fastapi import FastAPI, Request, HTTPException, status, Header, Form, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import Annotated
import uvicorn

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
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

signed_in_state = False


def set_signed_in_state(state: bool):
    global signed_in_state
    signed_in_state = state


def get_signed_in_state() -> bool:
    return signed_in_state


@app.get("/", response_class=HTMLResponse)
async def root(
    request: Request,
):
    return templates.TemplateResponse("home.html", {"request": request})


@app.post("/signin", response_model=User)
async def signin(
    username: str = Form(None, description="Username"),
    password: str = Form(None, description="Password"),
):
    set_signed_in_state(True)
    if not username or not password:
        raise HTTPException(
            status_code=422, detail="Username or password cannot be empty"
        )

    user_data = fake_users_db.get(username)

    if user_data is None or user_data["password"] != password:
        raise HTTPException(
            status_code=401, detail="Username or password is not correct"
        )
    return RedirectResponse(url="/menber", status_code=status.HTTP_303_SEE_OTHER)


@app.middleware("http")
async def verify_signed_in_state(request: Request, call_next):
    if request.url.path == "/menber" and not get_signed_in_state():
        return RedirectResponse(url="/")
    response = await call_next(request)
    return response


async def http_exception_handler(request: Request, exc: HTTPException):
    if exc.status_code == 401 or exc.status_code == 422:
        error_message = "Username or password is not correct"
        return RedirectResponse(
            url=f"/error?message={error_message}", status_code=status.HTTP_303_SEE_OTHER
        )


app.add_exception_handler(HTTPException, http_exception_handler)


@app.get("/error")
async def error(request: Request, message: str = None):
    return templates.TemplateResponse("error.html", {"request": request})


@app.get("/menber")
async def menber(request: Request):
    return templates.TemplateResponse("menber.html", {"request": request})


@app.get("/signout")
async def signout(request: Request):
    set_signed_in_state(False)
    return RedirectResponse(url="/", status_code=status.HTTP_307_TEMPORARY_REDIRECT)


@app.get("/square/{number}")
async def square_number(request: Request, number: int):
    squared_number = number * number
    return templates.TemplateResponse(
        "square.html", {"request": request, "squared_number": squared_number}
    )


if __name__ == "__main__":
    uvicorn.run(app="main:app", host="127.0.0.1", port=8000, reload=True)
