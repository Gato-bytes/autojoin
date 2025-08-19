from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Job API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class JobData(BaseModel):
    money: str
    name: str
    players: str
    scriptJoinPC: str

jobs = []

@app.post("/job")
async def add_job(data: JobData):
    global jobs
    jobs.insert(0, {
        "money": data.money,
        "name": data.name,
        "players": data.players,
        "script": data.scriptJoinPC
    })
    jobs = jobs[:150]
    return {"message": "Job adicionado", "jobs": jobs}

@app.get("/job")
async def get_jobs():
    return {"jobs": jobs}
