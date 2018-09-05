import discord
import random
from discord.ext import commands
from discord import Embed

bot = commands.Bot(command_prefix='$', description='Si quieres poder hacer una tirada escribe *$roll nivel_habilidad*')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def roll(ctx, *args):

    rollresult = dices()

    mediumresult = sorted(rollresult)[1]

    if len(args) > 0:
        skill = int(args[0])
        total = mediumresult + skill

        rich=Embed(title="El resultado de la tirada de {0.author.display_name} es **{1}**".format(ctx, total))
        rich.add_field(name="tirada", value=rollresult, inline=True)
        rich.add_field(name="dado medio", value=mediumresult, inline=True)
        rich.add_field(name="resultado", value="{0} + {1} = {2}".format(mediumresult, skill, total), inline=False)

        await ctx.send(embed=rich)
    else:
        rich=Embed(title="El resultado de la tirada de {0.author.display_name} es **{1}**".format(ctx, mediumresult))
        rich.add_field(name="tirada", value=rollresult, inline=True)
        rich.add_field(name="dado medio", value=mediumresult, inline=True)

        await ctx.send(embed=rich)

def dices():
    min = 1
    max = 10

    result = []

    for _ in range(3):
        result.append(random.randint(min, max))

    return result


bot.run('NDg2NTE2OTU1MDgwMDMyMjU3.DnAVeQ.D3i-Xgr715KvME3knB94KF-0Rv8')