from fastapi import FastAPI # pyright: ignore[reportMissingImports]

app = FastAPI()


@app.get("/")
def root():
    return ["Hello,", " World!"]