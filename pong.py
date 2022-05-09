
from nextcord.ext import commands
TOKEN = "OTcxODk2MjY3NzQ1Njg1NTk1.GXqvp9.X2YgwcjQZRBB7qWmgPcQYjHgJ_9cmnH_Iqg-Is"    
bot= commands.Bot(command_prefix="$")

@bot.command()
async def ping(ctx: commands.Context):
    await ctx.send("pong")
    print("pong")
    print("hi")
bot.run(TOKEN)