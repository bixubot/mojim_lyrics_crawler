import os
import json

LYRICS_DIR = '.\lyrics'

lyrics = []
for f in os.listdir(LYRICS_DIR):
    if f.endswith(".txt"):
        with open(os.path.join(LYRICS_DIR, f), 'r', encoding='utf-8') as lyrics_file:
            lyrics += lyrics_file.read().split(';')

lyrics = list(filter(None, lyrics))
print("There are %s lyrics in total." % len(lyrics))
with open('train.json', 'w', encoding='utf-8') as f:
    json.dump(lyrics, f, ensure_ascii=False)
