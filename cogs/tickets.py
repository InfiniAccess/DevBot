import discord
from discord.ext import commands
import pymongo
from pymongo import MongoClient

mongoConnect = open("mongoconnect.txt", "r").read()
cluster = MongoClient(mongoConnect)
db = cluster["TicketDB"]
collection = db["TicketCol"]


class Tickets(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Loaded Ticket module.")

    @commands.command()
    async def createTicketChannel(self, ctx):
        await ctx.channel.purge(limit=1)

        ticketEmbed = discord.Embed(
            title="Support Ticket",
            description="To create a ticket react with ✉️",
            colour=discord.Colour.red(),
        )

        message = await ctx.channel.send(embed=ticketEmbed)
        await message.add_reaction("✉️")
        self.reacted_message = message

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        print(reaction.count)

    # This part gets the count of how many reactions there are. We will use this to be able to create a ticket and then remove that person's reaction.


def setup(client):
    client.add_cog(Tickets(client))