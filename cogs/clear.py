import discord
from discord.ext import commands


class Clear(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Loaded clear cog module.")

    @commands.command()
    async def clear(self, ctx):
        if ctx.message.content[7:] == "all":
            await ctx.channel.purge()
        else:
            await ctx.channel.purge(limit=int(ctx.message.content[7:]))


def setup(client):
    client.add_cog(Clear(client))