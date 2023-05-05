setup the bot in https://discord.com/developers/applications/

cpy the token and use it in your code and run it

#Adding TOKEN
copy the token from developer portel and paste to a new file extention as {.env}
and make a variable {TK} pointing towards main.py

#Additional info for python langaage
Using intents in discord.py

Intents are a feature of Discord that tells the gateway exactly which events to send your bot. Various features of discord.py rely on having particular intents enabled, further detailed in its documentation. Since discord.py v2.0.0, it has become mandatory for developers to explicitly define the values of these intents in their code.

There are standard and privileged intents. To use privileged intents like Presences, Server Members, and Message Content, you have to first enable them in the Discord Developer Portal. In there, go to the Bot page of your application, scroll down to the Privileged Gateway Intents section, and enable the privileged intents that you need. Standard intents can be used without any changes in the developer portal.

Afterwards in your code, you need to set the intents you want to connect with in the bot's constructor using the intents keyword argument, like this:
from discord import Intents
from discord.ext import commands

# Enable all standard intents and message content
# (prefix commands generally require message content)
intents = Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

For more info about using intents, see discord.py's related guide, and for general information about them, see the Discord developer documentation on intents.
