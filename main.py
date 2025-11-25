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

class Personagem():
    def __init__(self,nome,nivel,job,hp):
        self.nome = nome
        self.nivel = nivel
        self.job = job
        self.hp = hp

class Arma():
    poder = 5
    nome = "Espada Olimpica"

espada = Arma()
personagens = []
armas = []
filmes = []


@bot.event
async def on_ready():
    print(f'Bot is online as {bot.user}')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

@bot.command()
async def hello(ctx):
    await ctx.send("Ola Marilene!")

#método para rolar dados
@bot.command()
async def roll_dice(ctx):
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
    
    await ctx.send("Escolha qual o dado vai rolar: 4,6,8,12,20")
    try:
        msg = await bot.wait_for("message",check=check,timeout=30.0)
        try:
            maxroll = int(msg.content)
            random_int = random.randint(1,maxroll)
            await ctx.send(f'Resultado do d{maxroll}: {random_int}')
        except ValueError:
                await ctx.send("O valor do dado deve ser apenas numérico!")
    except asyncio.TimeoutError:
        await ctx.send("Voce demorou demais para responder!")

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
        filmes.append(favorite_movie)
    except asyncio.TimeoutError:
        await ctx.send("perdão, demorou demais pra responder!")

@bot.command()
async def adicionar_arma(ctx,nome,poder):
    nova_arma = Arma()
    nova_arma.nome = nome
    nova_arma.poder = poder
    armas.append(nova_arma)
    
    for arma in armas:
        await ctx.send(f'O nome da arma é {arma.nome} e seu poder de ataque é {arma.poder}')

    await ctx.send("Fim da lista de armas")

@bot.command()
async def listar_armas(ctx):
    if len(armas) == 0:
        await ctx.send(f'a lista de armas está vazia')
    
        for arma in armas:
            await ctx.send(f'Nome: {arma.nome}, Poder: {arma.poder}')

@bot.command()
async def listar_filmes(ctx):
    for filme in filmes:
        await ctx.send(f'Filme: {filme}')
#comando para criar personagem basico
@bot.command()
async def criar_personagem(ctx):
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
    await ctx.send("Qual o nome do seu personagem? ")
    msg = await bot.wait_for("message",check=check,timeout=30.0)
    nome_personagem = msg.content
    await ctx.send("Qual o nivel do seu personagem? ")
    msg = await bot.wait_for("message",check=check,timeout=30.0)
    nivel = int(msg.content)
    await ctx.send("Qual a classe do seu personagem? ")
    msg = await bot.wait_for("message",check=check,timeout=30.0)
    job = msg.content
    await ctx.send("Qual o hp do seu personagem? ")
    msg = await bot.wait_for("message",check=check,timeout=30.0)
    hp = int(msg.content)
    novo_personagem = Personagem(nome_personagem,nivel,job,hp)
    personagens.append(novo_personagem)
    await ctx.send(f"Personagem '{nome_personagem}' criado com sucesso!")
    
#comando para listar personagens
@bot.command()
async def listar_personagens(ctx):
    for personagem in personagens:
        await ctx.send(f'Nome: {personagem.nome}, Nível: {personagem.nivel}, Classe: {personagem.job}, HP: {personagem.hp}')


bot.run(bot_token)
