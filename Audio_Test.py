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

print(transcription.words)



#for word in trascription.words:
#   print(f"{(word.start * 1000):.0f}\t{(word.end * 1000):.0f}\t{word.word}")
