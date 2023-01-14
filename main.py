import discord
from discord import app_commands
import os
from dotenv import load_dotenv
from neuralintents import GenericAssistant


chatbot = GenericAssistant('struct.json')
chatbot.train_model()
chatbot.save_model()

print("Bot running...")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

load_dotenv()
TOKEN = os.getenv('TK')

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event

async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith(">"):
        response =  chatbot.request(message.content[1:])
        await message.channel.send(response)
        #pass

client.run(TOKEN)