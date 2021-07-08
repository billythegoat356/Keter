import discord, time
from discord.ext.commands import Bot
from src.verif import code_verify
import asyncio

token = "ODYyNjUyMDU0NDc5Njk5OTk5.YObdVQ.MQFTFhnNT68SmkB-RcCVdJS4Tl4"

botOpt={"logo": "https://orig00.deviantart.net/5c2f/f/2013/337/6/9/69d144a62410c5b34c8ad53b39804e7d-d6r7x9f.gif",
        "BotName": "Keter",
        "welcomeMsg":"*verify to be verified",
        "role":"verified",
        "blank":"https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/Blank_button.svg/1124px-Blank_button.svg.png"}

intents = discord.Intents.default()
intents.members = True


keter = Bot(command_prefix = "keter", description = "keter", intents=intents)





verified = {}




 00:01:06 bash Fri Jul 09 - 2 | ~/Desktop/pull requests/Keter 
@keter.event
async def on_ready():
    await keter.change_presence(activity=discord.Game(name='*help'))
    print("Ready!")



@keter.listen()
async def on_message(message):

    content = message.content.split(" ")
    
    author = message.author
    channel = message.channel


    if author.id in verified and verified[author.id][0] == False:
        if message.content == verified[author.id][1]:
            embeded = discord.Embed(title=botOpt["BotName"], description='you have been verified', color=0xEE8700)
            embeded.set_thumbnail(url="https://media.giphy.com/media/sq3SxQclLXzRC/giphy.gif")
            msg = await channel.send(embed=embeded)
            role = discord.utils.get(author.guild.roles, name=botOpt["role"])
            await author.add_roles(role)
            del verified[author.id]
            await asyncio.sleep(10)
            await msg.delete()
        else:
            msg = await channel.send(content="Code invalide!")
            await asyncio.sleep(5)
            await msg.delete()
        await message.delete()
    if message.content == "*help":
        embeded = discord.Embed(title=botOpt["BotName"], description='Help', color=0xEE8700)
 00:03:59 bash Fri Jul 09 - 3 | ~/Desktop/pull requests/Keter 
        embeded.add_field(name="** *verify **", value="Verify your account", inline=True)
        embeded.add_field(name="** *welcome **", value="Send the message for new person", inline=True)
        await channel.send(embed=embeded)
    if message.content == "*welcome":
        await message.delete()
        embeded = discord.Embed(title=botOpt["welcomeMsg"], description='', color=0xEE8700)
        embeded.set_author(name=botOpt["BotName"],icon_url=botOpt["blank"])
        embeded.set_thumbnail(url=botOpt["logo"])
        embeded.set_footer(text="wait 30s befor send the code") 
        await channel.send(embed=embeded)
    if message.content == "*verify":
        await message.delete()
        code = await code_verify(channel)
        verified[author.id] = [False, code]


keter.run(token)
