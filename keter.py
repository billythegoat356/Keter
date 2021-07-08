import discord
from discord.ext.commands import Bot
from src.verif import code_verify



token = "TOKEN"


intents = discord.Intents.default()
intents.members = True


keter = Bot(command_prefix = "keter", description = "keter", intents=intents)





verified = {}





@keter.event
async def on_ready():
    await keter.change_presence(activity=discord.Game(name='src -> github.com/billythegoat356/Keter'))
    print("Ready!")



@keter.listen()
async def on_message(message):

    content = message.content.split(" ")
    
    author = message.author
    channel = message.channel

    print(message.content)

    if author.id in verified and verified[author.id][0] == False:
        if message.content == verified[author.id][1]:
            await channel.send(content="Vous êtes maintenant vérifié!")
            del verified[author.id]
        else:
            await channel.send(content="Code invalide!")



    if message.content == "*verify":
        code = await code_verify(channel)
        verified[author.id] = [False, code]













keter.run(token)