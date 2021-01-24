import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix="!")

token = open("token.txt", "r").read()


@client.event
async def on_ready():
    print("Bot is ready...")


@client.event
async def on_member_join(member):
    print(f"How did you get in here {member}?!")


@client.event
async def on_member_remove(member):
    print(f"Oh, {member} has left!")


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


@client.command()
async def showCogs(ctx):
    await ctx.send("The current cogs: ")
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await ctx.send(f"{filename[:-3]}")


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")


client.run(token)
