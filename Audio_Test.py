from openai import OpenAI
from config import api_key

client = OpenAI(api_key=api_key)

def print_word_timings():
    audio_path = "./Audio/q_isso_renan.mp3"
    with open(audio_path, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            file=audio_file,
            model="whisper-1", 
            response_format="verbose_json",
            timestamp_granularities=["word"]
        )
    return [
        {
            "start_ms": int(word.start * 1000),
            "end_ms": int(word.end * 1000),
            "word": word.word
        }
        for word in transcription.words
    ]