import settings_voice
from builtins import dict 

voice = settings_voice.speech({
    'key': 'a626706d4bc84bcdbeaa1b39a669376c',
    'hl': 'cs-cz',
    'v': 'Josef',
    'src': 'Je to vzor mužského hlasu. Líbí se to?',
    'r': '0',
    'c': 'mp3',
    'f': '44khz_16bit_stereo',
    'ssml': 'false',
    'b64': 'false'
     })

d1 = dict(voice)
print(d1)

x = d1["response"]
print(x)


#download and save mp3 file on disk
with open("muzsky_hlas.mp3", "wb") as f:
    f.write(x)