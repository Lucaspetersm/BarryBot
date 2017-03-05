import re #eeeeee
import random

nsfw_sub_list = []
furry_sub_list = []

with open("nsfw_sub_list.txt", 'r', encoding="utf-8") as f:
    nsfw_sub_list = f.read().splitlines()

with open("furry_sub_list.txt", 'r', encoding="utf-8") as f:
    furry_sub_list = f.read().splitlines()

#rule syntax: (function, regex search, channel blacklist, channel whitelist)
#channel blacklist and whitelist should be tuples
#leave channel whitelist empty to disable

command_rules = (
(get_meme, "^!getmeme"),
(get_porn, "^!getporn", ("general",)),
(get_keem, "^!getkeem"),
(get_dick, "^!getdick"),
(get_furry_porn, "^!getfurryporn", ("general",))
)

general_rules = (
(joy_spam, "😂"),
(right_there, "right there"),
(hello_faggot, "hello!"),
(boi_spam, "boi"),
(high_noon, "what(?: (?:time'?s|time is) it|(?:'?s| is) the time)\\?"),
(kkk_did_nothing_wrong, '.'),
(nice_meme, '.', (), ("m3m3z",))
)

def on_message(discord, reddit, message, channel):
    def good_channel(rule, channel):
        return (len(rule) < 2 or                           #  no blacklist or whitelist, or
                ((channel not in rule[2]) and              # (not in blacklist and
                 ((len(rule) < 3) or                       # (no whitelist or
                  (not rule[3]) or (channel in rule[3])))) #  in whitelist))
    
    def re_evaluate(exp, body):
        return re.search(exp, body, re.IGNORECASE) is not None
    
    channel = message.channel
    body = message.content
    
    for rule in command_rules:
        if good_channel(rule, channel) and re_evaluate(rule[1], body):
            rule[0](discord, reddit, message, channel)
            break
            
    for rule in general_rules:
        if good_channel(rule, channel) and re_evaluate(rule[1], body):
            rule[0](discord, reddit, message, channel)

def filter_links(submissions, min_score=0):
    #This will be part of a larger function/class which caches submissions soon.
    
    submissions = list(submissions)
    
    for s in submissions:
        if s.is_self or s.score < min_score:
            submissions.remove(s)
    
    return tuple(submissions)

# Command Definitons

def get_meme(discord, reddit, message, channel):
    submissions = filter_links(reddit.get_subreddit("dankmemes").get_hot(limit=100))
    url = submissions[random.randrange(0, len(submissions))].url
    
    response = '''Initializing Dank MayMays

MayMay Level: `[----____]` 25%

MayMay Level: `[------__]` 50%

MayMay Level: `[--------]` 100%

Commencing Meme: ''' + url
    
    await discord.send_message(channel, response.format(message))

def get_porn(discord, reddit, message, channel):
    subreddit = random.choice(nsfw_sub_list)
    submissions = filter_links(reddit.get_subreddit(subreddit).get_hot(limit=5))
    response = submissions[random.randrange(0, len(submissions))].url
    
    await discord.send_message(channel, response.format(message))

def get_keem(discord, reddit, message, channel):
    submissions = filter_links(reddit.get_subreddit("KeemGnome").get_top_from_all(limit=100))
    url = submissions[random.randrange(0, len(submissions))].url
    
    response = ("WHATS UP GUYS IT'S KILLLLLLLEEEEEEEEEERRRRRRRRR KEEEEEEEEEMMMMMMMMSSSSSSTTTTTAAARRRRRRRR " +
                url + 
                "\n\nLEEEETTTTSSS GEEEEETTTT RIIIIGHT INTOOOOO THE NEEEWWWSSSS")
    
    await discord.send_message(channel, response.format(message))

def get_dick(discord, reddit, message, channel):
    submissions = filter_links(reddit.get_subreddit("dickpics").get_hot(limit=100), min_score=3)
    response = submissions[random.randrange(0, len(submissions))].url
    
    await discord.send_message(channel, response.format(message))

def get_furry_porn(discord, reddit, message, channel):
    subreddit = random.choice(furry_sub_list)
    submissions = filter_links(reddit.get_subreddit(subreddit).get_hot(limit=25))
    response = submissions[random.randrange(0, len(submissions))].url
    
    await discord.send_message(channel, response.format(message))

# General Response Definitons

def joy_spam(discord, reddit, message, channel):
    response = ':joy:'*400
    await discord.send_message(channel, response.format(message))

def right_there(discord, reddit, message, channel):
    response = ":ok_hand::ok_hand::ok_hand: right:heavy_check_mark:there :heavy_check_mark::heavy_check_mark:if i do ƽaү so my self :100: i say so :100: thats what im talking about right there right there (chorus: ʳᶦᵍʰᵗ ᵗʰᵉʳᵉ) mMMMMᎷМ:100: :ok_hand::ok_hand: :ok_hand:НO0ОଠOOOOOОଠଠOoooᵒᵒᵒᵒᵒᵒᵒᵒᵒ:ok_hand: :ok_hand::ok_hand: :ok_hand: :100: :ok_hand: :eyes: :eyes: :eyes: :ok_hand::ok_hand:Good shit"
    
    await discord.send_message(channel, response.format(message))

def hello_faggot(discord, reddit, message, channel):
    response = "Fuck you faggot"
    await discord.send_message(channel, response.format(message))

def boi_spam(discord, reddit, message, channel):
    response = 'i'*1000
    await discord.send_message(channel, response.format(message))

def high_noon(discord, reddit, message, channel):
    response = "It's high noon!"
    await discord.send_message(channel, response.format(message))

def kkk_did_nothing_wrong(discord, reddit, message, channel):
    if random.randrange(0, 1000) == 0:
        response = "The KKK did nothing wrong!"
        await discord.send_message(channel, response.format(message))

def nice_meme(discord, reddit, message, channel):
    response = "nice meme"
    await discord.send_message(channel, response.format(message))