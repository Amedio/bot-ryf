import discord
import random
import utils
import ryf
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
    bonus = 0
    difficulty = 0
    dice_index = 1

    if len(args) == 1 and utils.is_int(args[0]):
        bonus = int(args[0])
    elif len(args) == 2 and utils.is_int(args[0]) and utils.is_int(args[1]):
        bonus = int(args[0])
        difficulty = int(args[1])
    elif len(args) == 3 and utils.is_int(args[1]) and utils.is_int(args[2]):
        bonus = int(args[1])
        difficulty = int(args[2])
    elif len(args) == 2 and utils.is_int(args[1]):
        bonus = int(args[1])

    dice_index = 1
    if len(args) > 0 and not utils.is_int(args[0]):
        if args[0] == 'down' or args[0] == 'd':
            dice_index = 0
        elif args[0] == 'up' or args[0] == 'u':
            dice_index = 2
    
    allrolls = []
    rollresult = dices()
    allrolls.append(rollresult)

    objective = sorted(rollresult)[dice_index]

    if objective == 1:
        if dice_index < 2:
            next = sorted(rollresult)[dice_index + 1]
            if next <= 5:
                rich=Embed(title="El resultado de la tirada de {0.author.display_name} es **PIFIA**".format(ctx))
                rich.add_field(name="tirada", value=allrolls, inline=False)
                rich.add_field(name="dado objetivo", value=objective, inline=True)
                rich.add_field(name="dado siguiente", value=next, inline=True)

                await ctx.send(embed=rich)
                return
        else:
            rich=Embed(title="El resultado de la tirada de {0.author.display_name} es **PIFIA**".format(ctx))
            rich.add_field(name="tirada", value=allrolls, inline=False)
            rich.add_field(name="dado objetivo", value=objective, inline=True)

            await ctx.send(embed=rich)
            return

    totalroll = objective

    while objective == 10:
        rollresult = dices()
        allrolls.append(rollresult)
        objective = sorted(rollresult)[dice_index]

        totalroll = totalroll + objective

    if bonus > 0 or difficulty > 0:
        total = totalroll + bonus

        rich=Embed(title="El resultado de la tirada de {0.author.display_name} es **{1}**".format(ctx, total))
        rich.add_field(name="tirada", value=allrolls, inline=True)
        rich.add_field(name="dado objetivo", value=totalroll, inline=True)
        rich.add_field(name="total", value="{0} + {1} = {2}".format(totalroll, bonus, total), inline=False)

        if difficulty > 0:
            if total >= difficulty:
                rich.add_field(name="resultado", value="ÉXITO", inline=True)
            else:
                rich.add_field(name="resultado", value="FALLO", inline=True)
            if total - difficulty >= 10:
                rich.add_field(name="crítico", value="CRÍTICO", inline=True)

        await ctx.send(embed=rich)
    else:
        rich=Embed(title="El resultado de la tirada de {0.author.display_name} es **{1}**".format(ctx, totalroll))
        rich.add_field(name="tirada", value=allrolls, inline=True)
        rich.add_field(name="dado objetivo", value=totalroll, inline=True)

        await ctx.send(embed=rich)

@bot.command()
async def damage(ctx, *args):
    rollresult = dices(6, int(args[0]))
    totalroll = 0
    for i in range(int(args[0])):
        totalroll = totalroll + rollresult[i]
    
    rich=Embed(title="El resultado de la tirada de {0.author.display_name} es **{1}**".format(ctx, totalroll))
    rich.add_field(name="tirada", value=rollresult, inline=True)
    rich.add_field(name="total", value=totalroll, inline=True)

    await ctx.send(embed=rich)

@bot.command()
async def effect(ctx, *args):
    rollresult = dices(6, int(args[0]))
    totalroll = 0
    for i in range(int(args[0])):
        totalroll = totalroll + rollresult[i]
    
    rich=Embed(title="El resultado de la tirada de {0.author.display_name} es **{1}**".format(ctx, totalroll))
    rich.add_field(name="tirada", value=rollresult, inline=True)
    rich.add_field(name="total", value=totalroll, inline=True)

    await ctx.send(embed=rich)

def dices(dicevalue=10,amount=3):
    min = 1
    max = dicevalue

    result = []

    for _ in range(amount):
        result.append(random.randint(min, max))

    return result

bot.run('NDg2NTE2OTU1MDgwMDMyMjU3.DnAVeQ.D3i-Xgr715KvME3knB94KF-0Rv8')