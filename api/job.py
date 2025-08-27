from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class JobData(BaseModel):
    jobIdMobile: str

current_job = ""

@app.post("/job")
async def update_job(data: JobData):
    global current_job
    current_job = data.jobIdMobile
    print(f"[UPDATE] jobIdMobile atualizado: {current_job}")
    return {"message": "JobIdMobile atualizado"}

@app.get("/job")
async def get_job():
    return {"jobIdMobile": current_job}
