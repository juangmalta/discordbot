TOKEN = "OTcxODk2MjY3NzQ1Njg1NTk1.GXqvp9.X2YgwcjQZRBB7qWmgPcQYjHgJ_9cmnH_Iqg-Is"  
from nextcord.ext import commands
from nextcord import Intents, Interaction

intents = Intents.all()
bot = commands.Bot(intents=intents)


@bot.slash_command(
    name="ping",
    description="pong!"
)
async def ex2(interaction: Interaction):
    await interaction.send("pong!")


bot.run(TOKEN)
