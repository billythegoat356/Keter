# -*- coding: utf-8 -*-


async def file_verification(file, author, key, max_size, user=None):

    content = (await file.read()).decode("cp850")

    if key in content.lower():

        if user:
            
            if max_size and file.size > max_size:
                await user.send(content=f"Fichier suspect envoyé de la part de {author.mention}! Mais le fichier dépassait la taille maximum autorisée de {max_size} avec une taille de {file.size}!")

            await user.send(content=f"Fichier suspect envoyé de la part de {author.mention}!", file=await file.to_file())

        
        return True
    
    return False

    


