from discord.ext import commands

def to_much_dices():
    async def predicate(ctx):
        print(ctx.args)
        return ctx.args[0] < 100
    return commands.check(predicate)