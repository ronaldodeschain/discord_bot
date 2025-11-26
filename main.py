import discord 
import random
import os
import asyncio
import json

from dotenv import load_dotenv
from discord.ext import commands

from models.personagem import Personagem

load_dotenv()
bot_token = os.getenv("BOT_TOKEN")
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix = '!',intents=intents)

#testes logicos
personagens = []
filmes = []

#distribuição de pontos de personagem
atributos = {'Força':8,'Destreza':8,'Constituição':8,'Inteligência':8,'Sabedoria':8,'Carisma':8}
pontos = 10

#distribuição de pontos de skill
dados = {'esquiva':0,'acrobacia':0,'diplomacia':0}
selecoes_skills = {}


@bot.event
async def on_ready():
    print(f'Bot is online as {bot.user}')

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

#teste para args
@bot.command()
async def processar(ctx,*inputs):
    #comando pra multiplos inputs enviados pelo user
    await ctx.send(f'processando {len(inputs)} enviados pelo usuario')
    for item in inputs:
        if isinstance(item,int):
            await ctx.send(f'{item} é um numero')
        await ctx.send(f'resolvendo o item {item}')

#testar await input e adição de item em lista
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
async def listar_filmes(ctx): #lista filmes
    for filme in filmes:
        await ctx.send(f'Filme: {filme}')

@bot.command()
async def criar_personagem(ctx): #comando para criar personagem basico
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

@bot.command()
async def listar_personagens(ctx): #comando para listar personagens
    for personagem in personagens:
        await ctx.send(personagem)

@bot.command()
async def colocar_pontos(ctx): #comando para testar logica de manipulação de pontos
    global pontos
    global atributos

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    while True:
        status_msg = f'Voce tem {pontos} para distribuir\n'
        for nome, valor in atributos.items():
            status_msg += f' - {nome}: {valor}\n'
        status_msg +="\nQual atributo deseja alterar?(ou digite 'sair' para terminar)"
        await ctx.send(status_msg)

        try:
            msg_atributo = await bot.wait_for("message",check=check,timeout=30.0)
            atributo_escolhido = msg_atributo.content.strip().capitalize()

            if atributo_escolhido.lower() == 'sair':
                await ctx.send("Saindo")
                break

            if atributo_escolhido not in atributos:
                await ctx.send(f"Atributo '{atributo_escolhido}' inválido.")
                continue
            
            await ctx.send(f'Voce quer aumentar ou diminuir {atributo_escolhido}?')
            msg_opcao = await bot.wait_for("message",check=check, timeout=30.0)
            opcao = msg_opcao.content.strip()

            #logica para aumentar
            if opcao == '+' or opcao.lower() == 'aumentar':
                if atributos[atributo_escolhido] < 14:
                    if pontos > 0:
                        pontos -= 1
                        atributos[atributo_escolhido] += 1
                        await ctx.send(f'{atributo_escolhido} aumentado para {atributos[
                            atributo_escolhido]}!')
                    else:
                        await ctx.send('voce não tem mais pontos para distribuir')
                else: 
                    await ctx.send(f'{atributo_escolhido} já está no valor máximo')
            elif opcao == '-' or opcao.lower() == 'diminuir':
                if atributos[atributo_escolhido]>8:
                    pontos += 1
                    atributos[atributo_escolhido] -= 1
                    await ctx.send(f'{atributo_escolhido} diminuido para {atributos[
                        atributo_escolhido]}')
                else: 
                    await ctx.send(f'{atributo_escolhido} já está no valor minimo')
            else:
                await ctx.send('Voce demorou demais. Distribuição cancelada')                    
            
        except asyncio.TimeoutError:
            await ctx.send("Voce demorou demais. Distribuição de pontos cancelada")
            break

@bot.command(name='escolher_skills')
async def escolher_skills(ctx, nome_personagem: str): #comando para selecionar skills
    # 1. Encontrar o personagem na sua lista
    personagem_encontrado = None
    for p in personagens:
        #Acessar os personagens através do json?
        if p.nome.lower() == nome_personagem.lower():
            personagem_encontrado = p
            break

    if not personagem_encontrado:
        await ctx.send(f"Personagem '{nome_personagem}' não encontrado. Crie um com `!criar_personagem` primeiro.")
        return

    # 2. Montar a lista de skills (similar ao seu comando !skills)
    descricao = 'Reaja com os emojis para escolher as skills do seu personagem.\n'
    descricao += 'Quando terminar, reaja com ✅ para confirmar.\n\n'
    
    emojis = ['1️⃣', '2️⃣', '3️⃣'] 
    for i, skill in enumerate(dados.keys()):
        descricao += f'{emojis[i]} - {skill}\n'

    embed = discord.Embed(
        title=f'Escolha de Skills para: {personagem_encontrado.nome}',
        description=descricao,
        color=discord.Color.gold()
    )
    embed.set_footer(text=f'Escolhendo skills para {personagem_encontrado.nome}')

    mensagem_skills = await ctx.send(embed=embed)

    # 3. Adicionar reações para o usuário clicar
    for i in range(len(dados)):
        await mensagem_skills.add_reaction(emojis[i])
    await mensagem_skills.add_reaction('✅') # Emoji de confirmação

    # 4. Armazenar informações para o evento on_reaction_add
    selecoes_skills[ctx.author.id] = {
        "personagem": personagem_encontrado,
        "mensagem_id": mensagem_skills.id,
        "skills_disponiveis": list(dados.keys()),
        "emojis": emojis
    }

@bot.event
async def on_reaction_add(reaction,user): #evento para salvar os dados da reação
    if user.bot: #ignora reações do bot
        return

    if user.id not in selecoes_skills: #verifica se a reação é válida
        return
    
    dados_selecao = selecoes_skills[user.id]

    if reaction.message.id != dados_selecao['mensagem_id']:
        return
    
    if str(reaction.emoji) == '✅': #verificar se foi clicado on V
        mensagem = await reaction.message.channel.fetch_message(reaction.message.id)

        skills_escolhidas = []
        for r in mensagem.reactions: #verifica se o usuário reagiu
            async for u in r.users():
                if u.id == user.id:
                    try: #encontrar qual skill o emoji pega
                        indice_emoji = dados_selecao['emojis'].index(str(r.emoji))
                        skill = dados_selecao['skills_disponiveis'][indice_emoji]
                        skills_escolhidas.append(skill)
                    except ValueError:
                        continue

        personagem = dados_selecao['personagem']

        dados_para_salvar = {
            'nome': personagem.nome,
            'nivel':personagem.nivel,
            'classe':personagem.job,
            'hp':personagem.hp,
            'skills': skills_escolhidas
        }
        nome_arquivo = f'{personagem.nome}.json'
        with open(nome_arquivo,'w',encoding='utf-8') as f:
            json.dump(dados_para_salvar,f,ensure_ascii=False, indent=4)

        await reaction.message.channel.send(f'Skills salvas para {personagem.nome}')

        del selecoes_skills[user.id]
        return
    
bot.run(bot_token)
