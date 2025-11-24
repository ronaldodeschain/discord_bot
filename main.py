import discord 
import random
import os
from dotenv import load_dotenv
from discord.ext import commands


load_dotenv()


bot_token = os.getenv("BOT_TOKEN")
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix = '!',intents=intents)

class arma():
    poder = 5
    nome = "Espada Olimpica"



espada = arma()



@bot.event
async def on_ready():
    print(f'Bot is online as {bot.user}')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

@bot.command()
async def hello(ctx):
    await ctx.send("Ola Marilene!")

@bot.command()
async def rolld20(ctx):
    random_int = random.randint(1,20)
    await ctx.send(f'Resultado do d20: {random_int}')

@bot.command()
async def arma(ctx):
    # Cria uma instância da sua classe
    await ctx.send(f'O nome da arma é {espada.nome} e seu poder de ataque é {espada.poder}')

@bot.command()
async def processar(ctx,*inputs):
    #comando pra multiplos inputs enviados pelo user
    await ctx.send(f'processando {len(inputs)} enviados pelo usuario')
    for item in inputs:
        if isinstance(item,int):
            await ctx.send(f'{item} é um numero')
        await ctx.send(f'resolvendo o item {item}')

bot.run(bot_token)
