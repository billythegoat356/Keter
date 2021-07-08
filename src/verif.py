from gtts import gTTS
from io import BytesIO
from discord import File
from random import choice
from string import ascii_uppercase, digits
from asyncio import sleep

chars = []


"""
for a in ascii_uppercase:
    chars.append(a)
"""    

for a in digits:
    chars.append(a)




async def code_verify(channel):

    code = "".join(choice(chars) for _ in range(6))

    print(code)

    f = BytesIO()

    code_file = gTTS(text=code.lower())

    code_file.write_to_fp(f)

    f.seek(0)

    fichier_say = File(f, "code.mp3")

    await channel.send(file=fichier_say)

    return code