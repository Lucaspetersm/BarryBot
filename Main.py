import discord, string, random, praw

from discord import opus

OPUS_LIBS = ['libopus-0.x86.dll', 'libopus-0.x64.dll', 'libopus-0.dll', 'libopus.so.0', 'libopus.0.dylib']

def load_opus_lib(opus_libs=OPUS_LIBS):
    if opus.is_loaded():
        return True
    for opus_lib in opus_libs:
        try:
            opus.load_opus(opus_lib)
            return
        except OSError:
            pass
    raise RuntimeError('Could not load an opus lib. Tried %s' % (', '.join(opus_libs)))
    
load_opus_lib()

if discord.opus.is_loaded():
  print("Loaded Opus")
else:
  print("Opus has not been loaded")

client = discord.Client()

r = praw.Reddit("Pull V1.0 by /u/Yalnix")
r.login("Username" "Password", disable_warning = True)


@client.event
async def on_message(message):
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
        lines = open('SubList').read().splitlines()
        myline = random.choice(lines)
        print(myline)
        sub_list = []
        submissions = r.get_subreddit(myline).get_top_from_all(limit=5)
        for submission in submissions:
            sub_list.append(submission)
        url2 = random.choice(sub_list)
        url = url2.url
        await client.send_message(message.channel, url)
        
    if message.content.startswith('!getkeem'):
        import random
        global myline
        submissions = r.get_subreddit("KeemGnome").get_top_from_all(limit=100)
        sub_list = []
        for submission in submissions:
            sub_list.append(submission)
        url2 = random.choice(sub_list)
        url = url2.url
        await client.send_message(message.channel, "WHATS UP GUYS IT'S KILLLLLLLEEEEEEEEEERRRRRRRRR KEEEEEEEEEMMMMMMMMSSSSSSTTTTTAAARRRRRRRR" + url)
        await client.send_message(message.channel, "LEEEETTTTSSS GEEEEETTTT RIIIIGHT INTOOOOO THE NEEEWWWSSSS")
    
    if message.content.startswith("!Voice"):
      channel = client.get_channel("255124792909234176")
      await client.join_voice_channel(channel)
      msg = client.is_voice_connected(channel)
      await client.send_message(message.channel, msg)
                
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run("MjQ0NjE5MDExMjQ0MDMyMDAw.CwAXbw.-ACD6cqZYawjzSeDlHJeC4KZmjU")
