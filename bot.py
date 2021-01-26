import discord
from discord.ext import commands
import os
import pymongo
from pymongo import MongoClient

mongoConnect = open("mongoconnect.txt", "r").read()
cluster = MongoClient(mongoConnect)
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
    await ctx.channel.send(f"Reloaded {extension} module.")


@client.command()
async def showModules(ctx):
    cogsEmbed = discord.Embed(
        title=f"Show Modules - Issued by {ctx.author}",
        description="All available modules that can be added.",
        colour=discord.Colour.green(),
    )

    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            cogsEmbed.add_field(name=f"{filename[:-3]}", value="Module", inline=False)
    await ctx.channel.send(embed=cogsEmbed)


@client.command()
async def loadAllModules(ctx):
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            client.load_extension(f"cogs.{filename[:-3]}")
    await ctx.channel.send("Loaded all available modules.")


@client.command()
async def listChannels(ctx):
    channelEmbed = discord.Embed(
        title="List Channels",
        description="Lists all channels in the server & their unique ids.",
        colour=discord.Colour.green(),
    )

    for channel in client.get_all_channels():
        channelEmbed.add_field(name=f"{channel}", value=f"{channel.id}", inline=False)

    await ctx.channel.send(embed=channelEmbed)


# @client.command()
# async def showCreators(ctx):
#     authorEmbed = discord.Embed(
#         title="Dev Work Bot",
#         description="A small project bot to work on different aspects of discord py.",
#         colour=discord.Colour.dark_red(),
#     )

#     authorEmbed.set_footer(text="This is a footer.")
#     authorEmbed.set_author(name="Sebastian, Deja")
#     authorEmbed.add_field(name="Field Name", value="Field Value", inline=False)
#     authorEmbed.add_field(name="Field Name", value="Field Value", inline=True)
#     authorEmbed.add_field(name="Field Name", value="Field Value", inline=True)

#     await ctx.channel.send(embed=authorEmbed)

# @client.command()
# async def checkJobs(ctx):
#     myquery = {"_id": ctx.author.id}

#     def check(m):
#         return m.author == ctx.author and m.channel == ctx.channel

#     if collection.count_documents(myquery) == 0:
#         await ctx.channel.send("Please enter your city:")
#         city = await client.wait_for("message", check=check)
#         await ctx.channel.send("Please enter the job title you are looking for:")
#         job = await client.wait_for("message", check=check)
#         post = {"_id": ctx.author.id, "City": city.content, "Job": job.content}
#         collection.insert_one(post)
#     else:
#         query = {"_id": ctx.author.id}
#         user = collection.find(query)
#         for result in user:
#             city = result["City"]
#             job = result["Job"]
#         await ctx.channel.send(f"Would you like to use {city} as your city? (Y/N)")
#         cityPrev = await client.wait_for("message", check=check)
#         if cityPrev.content.lower() == "y" or "yes":
#             await ctx.channel.send(f"Okay, we will use {city} to search for jobs.")
#         if cityPrev.content.lower() == "n" or "no":
#             await ctx.channel.send("Please enter your city:")
#             city = await client.wait_for("message", check=check)
#             collection.update_one(
#                 {"_id": ctx.author.id}, {"$set": {"City": city.content}}
#             )


client.run(token)
