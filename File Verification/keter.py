# -*- coding: utf-8 -*-

import discord
from discord.ext import commands

from src.file_verification import file_verification


# Le token de votre Bot Discord:
token = "TOKEN"

# Les mots bannis dans les fichiers envoyés, par défaut 'token':
key = "token"

# Fichiers autorisés, laisser vide pour enlever la restriction:
authorized = ['py', 'txt', 'png', 'jpg', 'jpeg', 'gif', 'mp3', 'mp4', 'json', 'bat']

# Voulez-vous recevoir les logs en message privé?
logs = False

# Votre identifiant Discord, si les logs sont activés:
user_logs = 0

# Taille maximum autorisée pour le renvoi des fichiers, si les logs sont activés:

# Exemple : 1KB = 1000 | 1MB = 1000000 | ∞ = 0

max_size = 100000

# N'oubliez pas de débloquer vos messages privés si les logs sont activés!


intents = discord.Intents.all()
intents.members = True



keter = commands.Bot( command_prefix= "keter", description= "keter", intents=intents)
keter.remove_command('help')




@keter.event
async def on_ready():
    global user_logs

    await keter.change_presence(activity=discord.Game(name='src -> github.com/billythegoat356/Keter'))
    print("Prêt!")


    user_logs = keter.get_user(user_logs) if logs else user_logs




@keter.listen()
async def on_message(message):

    author = message.author
    channel = message.channel

    if author.bot:
        return

    for file in message.attachments:
        if len(authorized) and file.content_type not in authorized:
                await message.delete()
                await channel.send(content=f"Mmmh, l'extension de ton fichier ne fait pas partie de celles autorisées {author.mention}!")
                return


        if await file_verification(file, author, key, max_size, user_logs) if logs else file_verification(file):
            await message.delete()
            await channel.send(content=f"Mmmh, ton fichier m'a l'air suspect {author.mention}!")



keter.run(token)
