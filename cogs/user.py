import discord
from discord.ext import commands


class User(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Loaded user cog module.")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f"How did you get in here {member}?!")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f"Oh, {member} has left!")


def setup(client):
    client.add_cog(User(client))