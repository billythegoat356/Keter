from gtts import gTTS
from io import BytesIO
from discord import File
from random import choice
from string import ascii_lowercase, digits
from asyncio import sleep
import time
codeuser = ""
chars = []
for a in ascii_lowercase:
    chars.append(a)
def generate_code():
    buf = ""
    for x in range(6):
        buf += choice(ascii_lowercase)
        buf += "."
    return buf
async def code_verify(channel):
    code = generate_code()
    f = BytesIO()
    code_file = gTTS(text=code.lower())
    code_file.write_to_fp(f)
    f.seek(0)
    fichier_say = File(f, "code.mp3")
    msg = await channel.send(file=fichier_say)
    codeuser = code.replace(".", "")
    print(codeuser)
    await sleep(30)
    await msg.delete()
    return code.replace(".","")
def get_code():
    return codeuser
