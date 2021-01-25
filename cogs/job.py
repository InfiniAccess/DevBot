import discord
from discord.ext import commands


class Job(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Loaded job cog module.")


def setup(client):
    client.add_cog(Job(client))
