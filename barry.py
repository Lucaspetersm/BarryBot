'''
    Barry Bot 2.0dev4
    
    A pretty nutty Discord bot.
    
    Originally authored by Yalnix.
    Contributors: unclepenguin, GarethPW.
    
    Licensed under Mozilla Public License Version 2.0.
'''

import platform, random, string, time
import discord, praw, youtube_dl
import commands, config
from discord import opus

ver = "2.0dev4"

user_agent = platform.system().lower() + ":pw.yalnix.barry:" + ver + " by /u/Yalnix"

OPUS_LIBS = ['libopus-0.x86.dll', 'libopus-0.x64.dll', 'libopus-0.dll', 'libopus.so.0', 'libopus.0.dylib']

def load_opus_lib(opus_libs=OPUS_LIBS):
    if not opus.is_loaded():    
        for opus_lib in opus_libs:
            try:
                opus.load_opus(opus_lib)
            except OSError:
                pass
            else:
                return
        else:
            raise RuntimeError('Could not load an opus lib. Tried %s' % (', '.join(opus_libs)))

#load_opus_lib()

if discord.opus.is_loaded():
  print("Loaded Opus")
else:
  print("Opus has not been loaded")

client = discord.Client()
general = discord.Client(id="228134125003866113") #General voice channel

reddit = praw.Reddit(user_agent)
reddit.login(config.reddit_user, config.reddit_pass, disable_warning=True)

@client.event
async def on_message(message):
    responses = []
    
    if message.author == client.user:
        return
    else:
        responses = commands.on_message(client, reddit, message)
    
    for msg in responses:
        await discord.send_message(message.channel, msg.format(message))

# TBI Music Bot Code

    #if message.content.startswith("!Voice"):
       # global voice
       # channel = client.get_channel("255124792909234176")
       # voice = await client.join_voice_channel(channel)
          
    #if message.content.startswith("!Stop"):
       # player.stop()
      
    #if message.content.startswith("!Disconnect"):
       # await voice.disconnect()
       # print("Disconnected")
      
    #if message.content.startswith("!Request"):
       # global player
       # searchforward = message.content
       # print(searchforward[9:])
       # player = await voice.create_ytdl_player(searchforward[9:])
       # msg = "{0} requested '{1}'".format(message.author,player.title)
       # await client.send_message(message.channel, msg)
       # player.start()
       # print(player.duration)
      #  time.sleep(player.duration)
      #  player.stop()
                    
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
   # global voice
   # channel = client.get_channel("255124792909234176")
   # voice = await client.join_voice_channel(channel)

client.run(config.discord_key)
