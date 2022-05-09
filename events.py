from nextcord.ext import commands
from nextcord import Intents, Message
TOKEN = "OTcxODk2MjY3NzQ1Njg1NTk1.GXqvp9.X2YgwcjQZRBB7qWmgPcQYjHgJ_9cmnH_Iqg-Is"    

intents = Intents.all()

bot = commands.Bot(command_prefix="$",intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} is online")
    
@bot.event
async def on_message(message:Message):
    if "thank" in message.content:
        await message.add_reaction("🍆")

bot.run(TOKEN)