from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

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
    for action in actions:
        print(action)
    return "Backend Success!"

if __name__ == "__main__":
    print("~ ~ ~ Main ~ ~ ~ ")
    # uvicorn.run(app, host="0.0.0.0", port=8000, access_log=False)