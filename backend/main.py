from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

from timeline import timeline_generator

origins = [
    "http://localhost",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    print("ok i printed root")
    return "ok i returned root!"

@app.post("/push-button")
async def push_button(request: Request):
    data = await request.json()
    actions = data.get("actions", [])
    timeline_generator(actions)

    return "Backend Success!"
