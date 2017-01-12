import discord, string, random, praw

client = discord.Client()

r = praw.Reddit("REDACTED")#Redacted will work but please name  it something more suitable that the Reddit API won't dislike
r.login("REDACTED", "REDACTED", disable_warning = True)#Where it Redacted please insert your own reddit username and password

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
        
                
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run("MjQ0NjE5MDExMjQ0MDMyMDAw.CwAXbw.-ACD6cqZYawjzSeDlHJeC4KZmjU")
