from bot_logic import gen_pass
from rnumber import r_number
import discord
import random


# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
client = discord.Client(intents=intents)




@client.event
async def on_ready():
    print('We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\\U0001f642")
    elif message.content.startswith('!пароль'):
        await message.channel.send(gen_pass(8))
    elif message.content.startswith('!номер любой'):
        await message.channel.send(r_number(1))
    elif message.content.startswith('!СТОП'):
        await message.channel.send('СТООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООООП')
    else:
        await message.channel.send(message.content)
        
@bot.command()    
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')



client.run('')
