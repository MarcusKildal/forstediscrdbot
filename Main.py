import discord
from discord.ext import commands

#bare kommandoen som eksempel !hjelp eller !info
client = commands.Bot(command_prefix='!')

#Forteller deg i terminalen at boten gikk på nettet
@client.event
async def on_ready():
    print('jeg er våken')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
        

    if message.content.startswith('fqcommands'):
        msg = '{0.author.mention}''\n ***The commands to this bots are ***' "\n  cheking".format(message)
        await message.author.send(msg)
    await client.process_commands(message)



#dette er min embed
@client.command()
async def info(ctx):
    embed=discord.Embed(title="Foeqo", description="A bot ***created*** by the one and only **Foeqo** this is a learning progres i also got dyslexia", color=discord.Color.red())

    embed.set_author(name= "secret, secret", icon_url= "https://img.pixers.pics/pho_wat(s3:700/FO/33/04/38/31/700_FO33043831_efa01b5895dd197c8e8f918bbe0f3afd.jpg,700,700,cms:2018/10/5bd1b6b8d04b8_220x50-watermark.png,over,480,650,jpg)/fototapeter-brann-font-bokstav-f.jpg.jpg")
    embed.add_field(name="Links",value="cheking" "\n  https://www.youtube.com/", inline=True)
    embed.set_thumbnail(url="https://img.pixers.pics/pho_wat(s3:700/FO/33/04/38/31/700_FO33043831_efa01b5895dd197c8e8f918bbe0f3afd.jpg,700,700,cms:2018/10/5bd1b6b8d04b8_220x50-watermark.png,over,480,650,jpg)/fototapeter-brann-font-bokstav-f.jpg.jpg")
    embed.set_image(url="https://img.pixers.pics/pho_wat(s3:700/FO/33/04/38/31/700_FO33043831_efa01b5895dd197c8e8f918bbe0f3afd.jpg,700,700,cms:2018/10/5bd1b6b8d04b8_220x50-watermark.png,over,480,650,jpg)/fototapeter-brann-font-bokstav-f.jpg.jpg")
    embed.set_footer(icon_url="https://img.pixers.pics/pho_wat(s3:700/FO/33/04/38/31/700_FO33043831_efa01b5895dd197c8e8f918bbe0f3afd.jpg,700,700,cms:2018/10/5bd1b6b8d04b8_220x50-watermark.png,over,480,650,jpg)/fototapeter-brann-font-bokstav-f.jpg.jpg", text = "created by Foeqo")
    await ctx.send(embed=embed)





#token for koden min VIS IKKE DET FOR FOLK. 
client.run('koden for min discord bot')
