import discord
from discord.ext import commands
import os
import pymongo
from pymongo import MongoClient


cluster = MongoClient("mongodb+srv://Holden:Access@devbotdb.3lgw9.mongodb.net/test")
db = cluster["UserData"]
collection = db["UserData"]

client = commands.Bot(command_prefix="!")

token = open("token.txt", "r").read()


@client.event
async def on_ready():
    print("Bot is ready.")


@client.command()
async def ping(ctx):
    await ctx.send(f"My latency is {round(client.latency * 1000)}ms!")


@client.command()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")


@client.command()
async def reload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    client.load_extension(f"cogs.{extension}")
    print(f"Reloaded {extension}.")


@client.command()
async def showCogs(ctx):
    await ctx.send("The current cogs: ")
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await ctx.send(f"{filename[:-3]}")


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")


@client.command()
async def checkJobs(ctx):
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

        # if collection.count_documents(myquery) == 0:

    await ctx.channel.send("Please enter your city:")
    city = await client.wait_for("message", check=check)
    await ctx.channel.send("Please enter the job title you are looking for:")
    job = await client.wait_for("message", check=check)
    print(job.content + " " + city.content)

    # post = {"_id": ctx.author.id, "City": city.content, "Job": job.content}
    # else:


client.run(token)
