import discord
from discord.ext import commands
import requests
import json

class clima():
    def __init__(self, client):
        self.client = client
    @commands.command()
    async def clima(self, ctx, *, buscar=None):

        if buscar is None:
           await ctx.send(f"Olá {ctx.author.mention}, vc precisa colocar o nome de uma cidade ou pais")
           return

        buscar = str(buscar).replace(" ", "%20")
        r = requests.get('http://api.apixu.com/v1/current.json?key=2d39dab5b1f64046ab6204301182912&q={buscar}')
        if r.status_code == 200:
           js = r.json()

        embed=discord.Embed(title="APIXU CLIMA", color=0xffff00)
        embed.add_field(name="Nome", value=str(js['location']['name']), inline=False)
        embed.add_field(name="Região", value=str(js['location']['region']), inline=True)
        await ctx.send(embed=embed)


def setup(client):
    print("[Comando clima] Carregado")
    client.add_cog(clima(client))
