from fastapi import FastAPI


app = FastAPI(title="Audio Transcription API", version="0.1")

@app.get("/")
def read_root():
    return {"status": "Backend Test OK"}
