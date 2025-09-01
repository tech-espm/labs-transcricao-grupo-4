from fastapi import FastAPI
from Audio_Test import print_word_timings
from fastapi.responses import JSONResponse


# LEMBRETE!!!!!!!! == SEMPRE QUE ABRIR A API NO NAEGADOR ADICIONAR /docs NO FINAL DO LINK 
# PARA VER A DOCUMENTAÇÃO AUTOMÁTICA
# EXEMPLO: http://http://127.0.0.1:8000/docs
app = FastAPI(title="Audio Transcription API", version="0.1")


    
def generate_JSON():
    word_timings = print_word_timings()
    return JSONResponse(content={word_timings}, status_code=200)

    
    
    
    
@app.get("/")
def word_timings():
    return print_word_timings()
