import openai
import json
from config import api_key
# Para criar o mockup
 
client = openai.OpenAI(api_key=api_key)
 
with open("voz.ogg", "rb") as audio_file:
	transcript = client.audio.transcriptions.create(
		model="whisper-1",
		file=audio_file,
		response_format="verbose_json",
		timestamp_granularities=["word"]
	)
 
with open("teste.json", "w", encoding="utf-8") as arquivo_json:
	lista = []
	for word in transcript.words:
		lista.append({
			"start": word.start,
			"end": word.end,
			"word": word.word
		})
	arquivo_json.write(json.dumps(lista))