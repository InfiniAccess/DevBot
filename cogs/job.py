import discord
from discord.ext import commands
import pymongo
from pymongo import MongoClient

mongoConnect = open("mongoconnect.txt", "r").read()
cluster = MongoClient(mongoConnect)
db = cluster["UserData"]
collection = db["JobSearchData"]


class Job(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Loaded Job module.")

    @commands.command()
    async def checkJobs(self, ctx):

        myquery = {"_id": ctx.author.id}

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        if collection.count_documents(myquery) == 0:
            await ctx.channel.send("Please enter your city:")
            city = await self.bot.wait_for("message", check=check)
            await ctx.channel.send("Please enter the job title you are looking for:")
            job = await self.bot.wait_for("message", check=check)
            post = {"_id": ctx.author.id, "City": city.content, "Job": job.content}
            collection.insert_one(post)
        else:
            query = {"_id": ctx.author.id}
            user = collection.find(query)
            for result in user:
                city = result["City"]
                job = result["Job"]
            await ctx.channel.send(f"Would you like to use {city} as your city? (Y/N)")
            cityPrev = await self.bot.wait_for("message", check=check)
            if cityPrev.content == "Y":
                await ctx.channel.send(f"Okay, we will use {city} to search for jobs.")
            if cityPrev.content == "N":
                await ctx.channel.send("Please enter your city:")
                city = await self.bot.wait_for("message", check=check)
                collection.update_one(
                    {"_id": ctx.author.id}, {"$set": {"City": city.content}}
                )


def setup(client):
    client.add_cog(Job(client))
