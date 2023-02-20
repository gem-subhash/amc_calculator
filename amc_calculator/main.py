from typing import List

import uvicorn


from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/calculator")
async def root(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request}
    )


@app.get("/calculator/sip")
async def root(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request}
    )

@app.get("/calculator/lumpsum")
async def root(request: Request):
    return templates.TemplateResponse(
        "lapsum.html", {"request": request}
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
