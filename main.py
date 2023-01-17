import discord
from discord.ext import commands
from discord.ext.commands import Bot
import time
import platform
import os
from dotenv import load_dotenv
from neuralintents import GenericAssistant
import random


chatbot = GenericAssistant('struct.json')
chatbot.train_model()
chatbot.save_model()

print("Bot running...")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='.', intents=intents)


load_dotenv()
TOKEN = os.getenv('TK')

@bot.tree.command(name="shutdown", description="Shuts down the Beta Bot")
async def shutdown(Interaction: discord.Interaction):
    await Interaction.response.send_message(content="Going down")
    print("Shutting down...")
    await bot.close()

@bot.tree.command(name="maths", description="I solve it")
async def math(interaction: discord.Interaction, expression:str):
    symbols = ['+', '-', '/', '*', '%']
    if any(s in expression for s in symbols):
        calculated = eval(expression)
        embed = discord.Embed(title="Math expression", description=f"`Expression` {expression}\n`Answer` {calculated}")
    else:
        await interaction.response.send_message("Bruh this is wrong")
    await interaction.response.send_message(embed=embed)


## secondary version of coinflip
#@bot.tree.command(name="coinflip", description="I flip it")
#@app_commands.choices(choices=[app_commands.Choice(name="Heads", value="heads"), app_commands.Choice(name="Tails", value="tails")])
#async def coinflip(interaction: discord.Interaction, choices:app_commands.Choice[str]):
    #values = ['heads','tails']
    #computerChoice = random.choice(values)
    #if choice not in values:
        #await interaction.response.send_message("Please do something bruh!")
    #if computerChoice == choices.value:
       # await interaction.response.send_message(f"yea u won, it was {choices}")
    #elif computerChoice == choices.value:
        #await interaction.response.send_message(f"yea u lost, it was {computerChoice}, lmao")
##

async def heads_or_tails(interaction, choice):
    computer_choice = random.choice(["heads", "tails"])
    if computer_choice == choice:
        await interaction.response.send_message(content=f"yea u won, it was {computer_choice}, shit :<")
    else:
        await interaction.response.send_message(content=f"yea u lost, it was {computer_choice}, haha lmao :>")

class Cf(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    @discord.ui.button(label="HEAD", style=discord.ButtonStyle.green)
    async def heads(self, interaction: discord.Interaction, Button: discord.ui.Button):
        await heads_or_tails(interaction, "heads")
    @discord.ui.button(label="TAIL", style=discord.ButtonStyle.blurple)
    async def tails(self, interaction: discord.Interaction, Button: discord.ui.Button):
        await heads_or_tails(interaction, "tails")

@bot.tree.command(name="coinflip", description="I flip it")
async def coinflip(interaction: discord.Interaction):
    await interaction.response.send_message(content="Please choose something man", view=Cf())

@bot.command()
async def roll(ctx, max:int=6):
    number = random.randint(1,max)
    await ctx.send(number)

@bot.event
async def on_ready():
    print(f'Online Mr.{bot.user}')
    synced = await bot.tree.sync()
    print("Slash CMDs Synced " + str(len(synced))+ " CMDs")

@bot.listen()
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content.startswith(">"):
        response = chatbot.request(message.content[1:])
        await message.channel.send(response)
        #pass

bot.run(TOKEN)
