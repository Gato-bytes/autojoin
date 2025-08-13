from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from mangum import Mangum  # Adaptador para serverless

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

handler = Mangum(app)  # Permite rodar em AWS Lambda / Vercel serverless
