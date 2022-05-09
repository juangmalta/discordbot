from discord import Guild, Member
from nextcord.ext import commands
from nextcord import Intents
TOKEN = "OTcxODk2MjY3NzQ1Njg1NTk1.GXqvp9.X2YgwcjQZRBB7qWmgPcQYjHgJ_9cmnH_Iqg-Is"    

intents=Intents.all()
bot=commands.Bot(command_prefix="$",intents=intents)

@bot.command()
async def ex1(ctx:commands.Context, id:int):
    guild=ctx.guild
    channel=guild.get_channel(972375394474922007)
    member=guild.get_member(id)
    await channel.send(f"Membe's nickname is: {member.display_name}")

bot.run(TOKEN) 