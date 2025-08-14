from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Permitir requisições CORS de qualquer origem
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Variável global para armazenar o jobIdMobile atual
current_job: str = ""

# Modelo de dados para o POST
class JobData(BaseModel):
    jobIdMobile: str

# Endpoint para atualizar o jobIdMobile
@app.post("/job")
async def update_job(data: JobData):
    global current_job
    current_job = data.jobIdMobile
    print(f"[UPDATE] jobIdMobile atualizado: {current_job}")
    return {"message": "JobIdMobile atualizado"}

# Endpoint para obter o jobIdMobile atual
@app.get("/job")
async def get_job():
    return {"jobIdMobile": current_job}
