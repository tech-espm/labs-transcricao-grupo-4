from fastapi import FastAPI
from Audio_Test import print_word_timings, get_word_timings_from_file_bytes
from fastapi.responses import JSONResponse
from fastapi import FastAPI, UploadFile, File
from openai import OpenAI
from config import api_key


# LEMBRETE!!!!!!!! == SEMPRE QUE ABRIR A API NO NAEGADOR ADICIONAR /docs NO FINAL DO LINK 
# PARA VER A DOCUMENTAÇÃO AUTOMÁTICA
# EXEMPLO: http://http://127.0.0.1:8000/docs
app = FastAPI(title="Audio Transcription API", version="0.2")
  

    
@app.get("/")
def word_timings():
    return print_word_timings()



@app.post("/upload-audio/")
async def upload_audio(file: UploadFile = File(...)):
    try:
        file_bytes = await file.read()
        timings = get_word_timings_from_file_bytes(file_bytes, file.filename)
        return JSONResponse(content=timings)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)