from openai import OpenAI
from config import api_key

client = OpenAI(api_key=api_key)
audio_file = open(".\Audio\q_isso_renan.mp3", "rb")

transcription = client.audio.transcriptions.create(
    file=audio_file,
    model="whisper-1", 
    response_format="verbose_json",
    timestamp_granularities=["word"]
)


#for word in transcription.words:
#   print(f"{(word.start * 1000):.0f}\t{(word.end * 1000):.0f}\t{word.word}")


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
            "start": word,
            "end": word,
            "word": word
        }
        for word in transcription.words
    ]
    
