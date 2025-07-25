import random
meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "NTP": "No te preocupes",
            "CHILL": "Relajarse, no preocuparse"
            }

word = input("Escribe una palabra que no entiendas: ").upper()

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    random_word = random.choice(meme_dict.keys())
    print("No está en el diccionario, pero tenemos: ", random_word, "que significa:", meme_dict[random_word])
