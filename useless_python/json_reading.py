import json
import openai
# Para ler o mockup
 
transcript = {
	"words": []
}
 
with open("mocado.json", "r", encoding="utf-8") as arquivo_json:
	transcript["words"] = json.loads(arquivo_json.read())



#for word in transcript["words"]:
#	print(f"{(word["start"] *1000):.0f}\t{(word["end"] * 1000):.0f}\t{word["word"]}")
 
 
 ## Script para separar em frases
 
 
 

# SEMPRE dar append, ao verificar a próxima "word_start" verificar o "word_end" anterior
# se a diferença for maior que X (ex: 0.5s) considerar que é uma nova frase

word_end = 0
phrase= []
lista = [phrase]
for word in transcript["words"]:
    word_start = word["start"] * 1000
    phrase.append(word["word"])

    if word_start - word_end >= 100:
        print(phrase)
        phrase = []
        lista.append(phrase)
    elif len(phrase) >= 5:
        print(phrase)
        phrase = []
        lista.append(phrase)

    word_end = word["end"] * 1000
    

#phrase = []
#count=0
#for word in transcript["words"]:
#    
#    phrase.append(word["word"])
#    count+=1
#    if count % 5 == 0:
#        print (phrase)
#        phrase.clear()