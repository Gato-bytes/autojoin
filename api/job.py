from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import base64

app = FastAPI()

current_job = "N/A"

# Modelo dos dados recebidos do cliente
class ClientData(BaseModel):
    userId: str
    hwid: str
    key: str

SECRET_EXTRA = "SegredoExtra"

# Função para decodificar a chave enviada pelo cliente
def decode_key(key: str, user_id: str, hwid: str) -> bool:
    try:
        # URL decode
        key = key.replace("%20", " ")  # simples URLDecode
        # Base64 decode
        b64_decoded = base64.urlsafe_b64decode(key.encode()).decode()
        # XOR inverso
        xor_bytes = bytearray(b64_decoded.encode())
        for i in range(len(xor_bytes)):
            xor_bytes[i] ^= 0x5A
        xor_str = xor_bytes.decode()
        # Validar se contém os dados corretos
        return user_id in xor_str and hwid in xor_str and SECRET_EXTRA in xor_str
    except Exception:
        return False

# Endpoint para receber dados do cliente
@app.post("/job")
async def update_job(data: ClientData):
    if not decode_key(data.key, data.userId, data.hwid):
        raise HTTPException(status_code=401, detail="Chave inválida")

    global current_job
    # Aqui você poderia gerar ou atualizar o jobIdMobile dinamicamente
    current_job = "ExemploJobID12345"
    print(f"[UPDATE] Dados recebidos: UserId={data.userId} HWID={data.hwid}")
    return {"message": "Dados recebidos com sucesso", "jobIdMobile": current_job}

# Endpoint GET simples para retornar o jobIdMobile
@app.get("/job")
async def get_job():
    return {"jobIdMobile": current_job}
