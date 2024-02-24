import discord
from discord.ext import commands
import os
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def map(ctx):
    await ctx.send('перейди по ссылке и увидишь где можно сдать мусор https://recyclemap.ru')
@bot.command()
async def mems(ctx):
    images1 = os.listdir('m2_l2/images')
    img_name = random.choice(images1)
    with open(f'm2_l2/images/{img_name}', 'rb') as f:
            picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)
@bot.command()
async def sos(ctx):
    await ctx.send('молодец ты сдал мусор напиши команду $mem и тебе выдаст смешную картинку с мусором')
    
bot.run('')
