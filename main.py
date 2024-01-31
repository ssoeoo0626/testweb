from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

# directory : 폴더 지정
templates = Jinja2Templates(directory="templates")

# @app.get("/")
@app.get("/", response_class=HTMLResponse)
async def main(request: Request):
    return templates.TemplateResponse(
        request = request, 
        name = "index.html",
        context = {
            "name" : 'IS'
        }
    )

@app.get("/hello")
async def hello():
    return "(fastapi) 안녕! 반가워!"

# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

# @app.get("/hello")
# async def root():
#     return {"message": "안녕! 반가워!"} 

# from fastapi import FastAPI, Request
# from fastapi.responses import HTMLResponse
# from fastapi.staticfiles import StaticFiles
# from fastapi.templating import Jinja2Templates

# app = FastAPI()

# templates = Jinja2Templates(directory="templates")

# @app.get("/hello")
# async def root():
#     return {"message": "Hello World"} 