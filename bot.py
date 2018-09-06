import discord
import random
from discord.ext import commands
from discord import Embed

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command(description='Para hacer una tirada prueba $roll [nivel_habilidad [dificultad]]')
async def roll(ctx, *args):

    allrolls = []
    rollresult = dices()
    allrolls.append(rollresult)

    objective = sorted(rollresult)[1]

    if objective == 1:
        next = sorted(rollresult)[2]
        if next <= 5:
            rich=Embed(title="El resultado de la tirada de {0.author.display_name} es **PIFIA**".format(ctx))
            rich.add_field(name="tirada", value=allrolls, inline=False)
            rich.add_field(name="dado objetivo", value=objective, inline=True)
            rich.add_field(name="dado siguiente", value=next, inline=True)

            await ctx.send(embed=rich)
            return

    totalroll = objective

    while objective == 10:
        rollresult = dices()
        allrolls.append(rollresult)
        objective = sorted(rollresult)[1]

        totalroll = totalroll + objective

    if len(args) > 0:
        skill = int(args[0])
        total = totalroll + skill

        rich=Embed(title="El resultado de la tirada de {0.author.display_name} es **{1}**".format(ctx, total))
        rich.add_field(name="tirada", value=allrolls, inline=True)
        rich.add_field(name="dado objetivo", value=totalroll, inline=True)
        rich.add_field(name="resultado", value="{0} + {1} = {2}".format(totalroll, skill, total), inline=False)

        if len(args) > 1:
            difficulty = int(args[1])
            if total - difficulty >= 10:
                rich.add_field(name="CRÍTICO", value="Ha sido crítico", inline=True)

        await ctx.send(embed=rich)
    else:
        rich=Embed(title="El resultado de la tirada de {0.author.display_name} es **{1}**".format(ctx, totalroll))
        rich.add_field(name="tirada", value=allrolls, inline=True)
        rich.add_field(name="dado objetivo", value=totalroll, inline=True)

        await ctx.send(embed=rich)

def dices():
    min = 1
    max = 10

    result = []

    for _ in range(3):
        result.append(random.randint(min, max))

    return result


bot.run('NDg2NTE2OTU1MDgwMDMyMjU3.DnAVeQ.D3i-Xgr715KvME3knB94KF-0Rv8')