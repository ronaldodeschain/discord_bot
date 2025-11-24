import discord 
import random
import os
import asyncio

from dotenv import load_dotenv
from discord.ext import commands


load_dotenv()


bot_token = os.getenv("BOT_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix = '!',intents=intents)

class Arma():
    poder = 5
    nome = "Espada Olimpica"



espada = Arma()



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

#testar await input
@bot.command()
async def ask(ctx):
    await ctx.send("Qual seu filme favorito?")

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
    
    try:
        msg = await bot.wait_for("message",check=check,timeout=30.0)
        favorite_movie = msg.content
        await ctx.send(f'Opa, {favorite_movie} é um ótimo filme!')
    except asyncio.TimeoutError:
        await ctx.send("perdão, demorou demais pra responder!")


bot.run(bot_token)
