import discord
from discord.ext import commands

client = commands.Bot(command_prefix="d!")
client.remove_command('help')

modulos = [
    "cogs.pic",
    "cogs.clima",
    "cogs.botinfo",
    "cogs.musica"
          ]

@client.event
async def on_ready():
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))
    await client.change_presence(activity=discord.Streaming(name="ESTOU SENDO DESENVOLVIDO CARAI ",url="https://www.twitch.tv/Yuka"))

if __name__ == '__main__':
 try:
   for modulo in modulos:
     client.load_extension(modulo)
 except Exception as e :
     print(f'[Erro] :  {e}')

client.run("NTE2OTkxMDY4NTIxMTAzMzcy.DwleAg.dV8Bdax720WkZ8wKOtDXUXxHw4M")