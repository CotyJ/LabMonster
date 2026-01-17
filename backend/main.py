from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/push-button")
async def push_button():
    return {"button": "pressed"}