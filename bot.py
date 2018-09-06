import discord
import random
import utils
import ryf
import asyncio
from discord.ext import commands
from discord import Embed
from checkers import to_much_dices

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
    
    roll_result = ryf.roll(dice_index)

    all_rolls = roll_result[0]
    total_roll = roll_result[1]
    critical_failure_next = 0
    if len(roll_result) == 3:
        critical_failure_next = roll_result[2]

    if total_roll == 1:
        rich=Embed(title="El resultado de la tirada de {0.author.display_name} es **PIFIA**".format(ctx))
        rich.add_field(name="tirada", value=all_rolls, inline=False)
        rich.add_field(name="dado objetivo", value=total_roll, inline=True)
        if critical_failure_next > 0:
            rich.add_field(name="dado siguiente", value=critical_failure_next, inline=True)

        await ctx.send(embed=rich)
        return

    total = total_roll + bonus

    rich=Embed(title="El resultado de la tirada de {0.author.display_name} es **{1}**".format(ctx, total))
    rich.add_field(name="tirada", value=all_rolls, inline=True)
    rich.add_field(name="dado objetivo", value=total_roll, inline=True)
    
    if bonus > 0 or difficulty > 0:
        rich.add_field(name="total", value="{0} + {1} = {2}".format(total_roll, bonus, total), inline=False)

        if difficulty > 0:
            if total >= difficulty:
                rich.add_field(name="resultado", value="ÉXITO", inline=True)
            else:
                rich.add_field(name="resultado", value="FALLO", inline=True)
            if total - difficulty >= 10:
                rich.add_field(name="crítico", value="CRÍTICO", inline=True)
                
    await ctx.send(embed=rich)

@bot.command()
async def damage(ctx, *args):
    dice_amount = int(args[0])
    if dice_amount >= 100:
        async with ctx.typing():
            await asyncio.sleep(3)
            await ctx.send("https://media.giphy.com/media/9JjnmOwXxOmLC/giphy.gif")
            return

    rollresult = dices(6, dice_amount)
    totalroll = 0
    for i in range(dice_amount):
        totalroll = totalroll + rollresult[i]
    
    rich=Embed(title="El resultado de la tirada de {0.author.display_name} es **{1}**".format(ctx, totalroll))
    rich.add_field(name="tirada", value=rollresult, inline=True)
    rich.add_field(name="total", value=totalroll, inline=True)

    await ctx.send(embed=rich)

@bot.command()
async def effect(ctx, *args):
    dice_amount = int(args[0])
    if dice_amount >= 100:
        async with ctx.typing():
            await asyncio.sleep(3)
            await ctx.send("https://media.giphy.com/media/9JjnmOwXxOmLC/giphy.gif")
            return
    rollresult = dices(6, dice_amount)
    totalroll = 0
    for i in range(dice_amount):
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