'''
    Barry Bot 2.0dev8
    
    A pretty nutty Discord bot.
    
    Originally authored by Yalnix.
    Contributors: unclepenguin, GarethPW.
    
    Licensed under Mozilla Public License Version 2.0.
'''

import platform, random, string, time
import discord, praw, youtube_dl
import commands, config
from discord import opus

ver = "2.1dev0"

user_agent = platform.system().lower() + ":pw.yalnix.barry:" + ver + " by /u/Yalnix"

client = discord.Client()
general = discord.Client(id="228134125003866113") #General voice channel

reddit = praw.Reddit(client_id='Q_LZxiXN7UVYyg',
                     client_secret='29Ce06E8FVjhVLeD-8u04MoSPK4',
                     password=config.reddit_pass,
                     user_agent=user_agent,
                     username=config.reddit_user) #Client_ID and Secret found on Pull_Bot Reddit Dev

print(reddit.user.me()) #Test to see if Login successful

@client.event
async def on_message(message):
    responses = []
    
    if message.author == client.user:
        return
    else:
        responses, delete = commands.on_message(client, reddit, message)
    
    if delete:
        try:
            await client.delete_message(message)
        except Exception:
            pass
    
    for msg in responses:
        await client.send_message(message.channel, msg.format(message))
                  
@client.event
async def on_ready():
    global voice
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(config.discord_key)
