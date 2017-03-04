'''
    Barry Bot 2.0dev1
    
    A pretty nutty Discord bot.
    
    Originally authored by Yalnix.
    Contributors: unclepenguin, GarethPW.
    
    Licensed under GNU General Public License v3.
'''

import discord, praw, random, string, time, youtube_dl
import commands, config
from discord import opus
from sys import exit as sysexit

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

load_opus_lib()

if discord.opus.is_loaded():
  print("Loaded Opus")
else:
  print("Opus has not been loaded")

client = discord.Client()
general = discord.Client(id="228134125003866113")

r = praw.Reddit("Pull V1.0 by /u/Yalnix")
r.login(config.reddit_user, config.reddit_pass, disable_warning=True)

@client.event
async def on_message(message):
    channel = message.channel
    if message.author == client.user:
        return

    if "😂" in message.content:
        msg = (':joy:'*400).format(message)
        await client.send_message(message.channel, msg)
    if "right there" in message.content.lower():
        msg = ":ok_hand::ok_hand::ok_hand: right:heavy_check_mark:there :heavy_check_mark::heavy_check_mark:if i do ƽaү so my self :100: i say so :100: thats what im talking about right there right there (chorus: ʳᶦᵍʰᵗ ᵗʰᵉʳᵉ) mMMMMᎷМ:100: :ok_hand::ok_hand: :ok_hand:НO0ОଠOOOOOОଠଠOoooᵒᵒᵒᵒᵒᵒᵒᵒᵒ:ok_hand: :ok_hand::ok_hand: :ok_hand: :100: :ok_hand: :eyes: :eyes: :eyes: :ok_hand::ok_hand:Good shit"
        await client.send_message(message.channel, msg)
    if "Hello!" in message.content:
        msg = ("Fuck you faggot")
        await client.send_message(message.channel, msg)
    if "boi" in message.content.lower():
        msg = "i"*1000
        await client.send_message(message.channel, msg)
    if "What time is it?" in message.content:
        await client.send_message(message.channel, "It's high noon!")
                  
    if message.content.startswith('!getmeme'):
        import random
        global myline
        submissions = r.get_subreddit("dankmemes").get_hot(limit=100)
        sub_list = []
        for submission in submissions:
            sub_list.append(submission)
        url2 = random.choice(sub_list)
        url = url2.url
        if "www.reddit.com" not in url:
          await client.send_message(message.channel, "Initializing Dank MayMays \n\nMayMay Level: `[----____]` 25% \n\nMayMay Level: `[------__]` 50% \n\nMayMay Level: `[--------]` 100% \n\nCommencing Meme: " + url)
        else:
          print("Self-Post")
    
    if message.content.startswith('!getporn'):
        import random
        global myline
        lines = open('sub_list.txt').read().splitlines()
        myline = random.choice(lines)
        print(myline)
        sub_list = []
        submissions = r.get_subreddit(myline).get_top_from_all(limit=5)
        for submission in submissions:
            sub_list.append(submission)
        url2 = random.choice(sub_list)
        url = url2.url
        await client.send_message(message.channel, url)
                
    if message.content.startswith('!getdick'):
        import random
        global myline
        submissions = r.get_subreddit("dickpics").get_hot(limit=100)
        sub_list = []
        for submission in submissions:
            sub_list.append(submission)
        url2 = random.choice(sub_list)
        url = url2.url
        if "www.reddit.com" not in url:
          await client.send_message(message.channel, "Initializing Dank Dicks \n\nMayMay Level: `[----____]` 25% \n\nDick Level: `[------__]` 50% \n\nDick Level: `[--------]` 100% \n\nCommencing Dick: " + url)
        else:
          print("Self-Post")
                    
    if message.content.startswith('!getfurryporn'):
        import random
        global myline
        lines = open('furry_sub_list.txt').read().splitlines()
        myline = random.choice(lines)
        print(myline)
        sub_list = []
        submissions = r.get_subreddit(myline).get_top_from_all(limit=500)
        for submission in submissions:
            sub_list.append(submission)
        url2 = random.choice(sub_list)
        url = url2.url
        await client.send_message(message.channel, url)
        
    if message.content.startswith('!getkeem'):
        import random
        submissions = r.get_subreddit("KeemGnome").get_top_from_all(limit=100)
        sub_list = []
        for submission in submissions:
            sub_list.append(submission)
        url2 = random.choice(sub_list)
        url = url2.url
        await client.send_message(message.channel, "WHATS UP GUYS IT'S KILLLLLLLEEEEEEEEEERRRRRRRRR KEEEEEEEEEMMMMMMMMSSSSSSTTTTTAAARRRRRRRR" + url)
        await client.send_message(message.channel, "LEEEETTTTSSS GEEEEETTTT RIIIIGHT INTOOOOO THE NEEEWWWSSSS")
 
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