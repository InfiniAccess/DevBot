import discord
from discord.ext import commands


class Job(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def checkJobs(self, ctx):
        channel = ctx.channel
        await channel.send("Please enter your city:")

        def is_location(m):
            return m.channel == channel and m.content

        location = await channel.wait_for("message", check=is_location)
        ctx.send(f"Your location is {location}?")


def setup(client):
    client.add_cog(Job(client))
