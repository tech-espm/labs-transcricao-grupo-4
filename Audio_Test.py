from openai import OpenAI
from config import api_key
import io

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
            "start": word.start,
            "end": word.end,
            "word": word.word
        }
        for word in transcription.words
    ]

    



def get_word_timings_from_file_bytes(file_bytes, filename):
    # Cria um buffer em memória a partir do arquivo enviado
    audio_buffer = io.BytesIO(file_bytes)
    audio_buffer.name = filename  # importante: define o nome com extensão correta
    
    transcription = client.audio.transcriptions.create(
        file=audio_buffer,
        model="whisper-1",
        response_format="verbose_json",
        timestamp_granularities=["word"]
    )
    
    return [
        {
            "start": word.start,
            "end": word.end,
            "word": word.word
        }
        for word in transcription.words
    ]




