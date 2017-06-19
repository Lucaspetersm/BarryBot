import re #eeeeee
import random

nsfw_sub_list = []
furry_sub_list = []

with open("sub_list/nsfw_sub_list.txt", 'r', encoding="utf-8") as f:
    nsfw_sub_list = f.read().splitlines()

with open("sub_list/furry_sub_list.txt", 'r', encoding="utf-8") as f:
    furry_sub_list = f.read().splitlines()

# Main Definitions

def on_message(discord, reddit, message):
    responses = []
    delete = False
    
    def good_channel(rule, channel):
        return (len(rule) < 3 or                           #  no blacklist or whitelist, or
                ((channel not in rule[2]) and              # (not in blacklist and
                 ((len(rule) < 4) or                       # (no whitelist or
                  (not rule[3]) or (channel in rule[3])))) #  in whitelist))
    
    def re_evaluate(exp, body):
        return re.search(exp, body, re.IGNORECASE) is not None
    
    channel = message.channel.name
    body = message.content
    
    for rule in command_rules:
        if good_channel(rule, channel) and re_evaluate(rule[1], body):
            rule[0](discord, reddit, responses, message, channel)
            break
            
    for rule in general_rules:
        if good_channel(rule, channel) and re_evaluate(rule[1], body):
            rule[0](discord, reddit, responses, message, channel)
            
    for rule in deletion_rules:
        if good_channel(rule, channel) and re_evaluate(rule[1], body):
            rule[0](discord, reddit, responses, message, channel)
            delete = True
            break
    
    return (responses, delete)

def filter_links(submissions, min_score=0):
    #This will be part of a larger function/class which caches submissions soon.
    
    submissions = list(submissions)
    
    for s in submissions:
        if s.is_self or s.score < min_score:
            submissions.remove(s)
    
    return tuple(submissions)

# Command Definitons

def get_meme(discord, reddit, responses, message, channel):
    submissions = filter_links(reddit.get_subreddit("dankmemes").get_hot(limit=100))
    url = submissions[random.randrange(0, len(submissions))].url
    
    response = '''Initializing Dank MayMays

MayMay Level: `[----____]` 25%

MayMay Level: `[------__]` 50%

MayMay Level: `[--------]` 100%

Commencing Meme: ''' + url
    
    responses.append(response)

def get_porn(discord, reddit, responses, message, channel):
    subreddit = random.choice(nsfw_sub_list)
    submissions = filter_links(reddit.get_subreddit(subreddit).get_hot(limit=5))
    response = submissions[random.randrange(0, len(submissions))].url
    
    responses.append(response)

def get_keem(discord, reddit, responses, message, channel):
    submissions = filter_links(reddit.get_subreddit("KeemGnome").get_top_from_all(limit=100))
    url = submissions[random.randrange(0, len(submissions))].url
    
    response = ("WHATS UP GUYS IT'S KILLLLLLLEEEEEEEEEERRRRRRRRR KEEEEEEEEEMMMMMMMMSSSSSSTTTTTAAARRRRRRRR " +
                url + 
                "\n\nLEEEETTTTSSS GEEEEETTTT RIIIIGHT INTOOOOO THE NEEEWWWSSSS")
    
    responses.append(response)

def get_dick(discord, reddit, responses, message, channel):
    submissions = filter_links(reddit.get_subreddit("dickpics").get_hot(limit=100), min_score=3)
    response = submissions[random.randrange(0, len(submissions))].url
    
    responses.append(response)

def get_furry_porn(discord, reddit, responses, message, channel):
    subreddit = random.choice(furry_sub_list)
    submissions = filter_links(reddit.get_subreddit(subreddit).get_hot(limit=25))
    response = submissions[random.randrange(0, len(submissions))].url
    
    responses.append(response)

# General Response Definitons

def joy_spam(discord, reddit, responses, message, channel):
    response = ':joy:'*400
    responses.append(response)

def right_there(discord, reddit, responses, message, channel):
    response = ":ok_hand::ok_hand::ok_hand: right:heavy_check_mark:there :heavy_check_mark::heavy_check_mark:if i do ƽaү so my self :100: i say so :100: thats what im talking about right there right there (chorus: ʳᶦᵍʰᵗ ᵗʰᵉʳᵉ) mMMMMᎷМ:100: :ok_hand::ok_hand: :ok_hand:НO0ОଠOOOOOОଠଠOoooᵒᵒᵒᵒᵒᵒᵒᵒᵒ:ok_hand: :ok_hand::ok_hand: :ok_hand: :100: :ok_hand: :eyes: :eyes: :eyes: :ok_hand::ok_hand:Good shit"
    
    responses.append(response)

def hello_faggot(discord, reddit, responses, message, channel):
    response = "Fuck you faggot"
    responses.append(response)

def boi_spam(discord, reddit, responses, message, channel):
    response = 'i'*1000
    responses.append(response)

def high_noon(discord, reddit, responses, message, channel):
    response = "It's high noon!"
    responses.append(response)

def kkk_did_nothing_wrong(discord, reddit, responses, message, channel):
    n = random.randrange(0, 10000)
    
    if n == 0:
        response = "The KKK did nothing wrong! (<@{0}>)".format(message.author.id)
        responses.append(response)
    elif n < 10:
        response = "The KKK did n... jk not rly get rekt cunt"
        responses.append(response)

def nice_meme(discord, reddit, responses, message, channel):
    response = "nice meme"
    responses.append(response)

def shit_automod(discord, reddit, responses, message, channel):
    response = ("What the fuck did you just fucking say about me, you НO0ОଠOOOOOОଠଠOoooᵒᵒᵒᵒᵒᵒᵒᵒᵒ? I’ll have you know I graduated top of my class in the :ok_hand: :eyes: good shit go౦ԁ sHit :ok_hand: academy, and I’ve been involved in numerous secret raids on :thumbsdown: Baaddd ShIT :thumbsdown: :thumbsdown: :thumbsdown: :thumbsdown: , and I have over 300 confirmed (chorus: ʳᶦᵍʰᵗ ᵗʰᵉʳᵉ) :ok_hand: :eyes: . I am trained in :ok_hand: :eyes: :ok_hand: :eyes: :ok_hand: :eyes: :ok_hand: :eyes: :ok_hand: :eyes: warfare and I’m the top shiter in the entire US armed mMMMMᎷМ:100: :ok_hand: . You are nothing to me but just another Baaa AaAadDddD Sh1t :thumbsdown: . I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, :100: thats what im talking about right there right there . You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of go౦ԁ sHit :ok_hand: across the USA and your IP is being traced right :ok_hand: :ok_hand: there :ok_hand: :ok_hand: :ok_hand: right:heavy_check_mark:there :heavy_check_mark:, so :heavy_check_mark:if i do ƽaү so my self :100: i say so :100:, you better prepare for the storm, НO0ОଠOOOOOОଠଠOoooᵒᵒᵒᵒᵒᵒᵒᵒᵒ :ok_hand: . The storm that wipes out the pathetic little thing you call your life. You’re fucking dead, kid. I can be anywhere, anytime, I could be right :ok_hand: :ok_hand: there :ok_hand: :ok_hand: :ok_hand: right:heavy_check_mark:there :heavy_check_mark: and I can kill you in over seven hundred ways, and that’s just with my bare (chorus: ʳᶦᵍʰᵗ ᵗʰᵉʳᵉ). Not only am I extensively trained in mMMMMᎷМ:100: :ok_hand: combat, but I have access to the entire arsenal of the United States :ok_hand: :ok_hand::ok_hand: :ok_hand: :100: :ok_hand: :eyes: :eyes: :eyes: :ok_hand::ok_hand:Good shit Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little BAAaAaAaAd shit.",
                "If only you could have known what unholy retribution your little “clever” comment was about to bring down upon you, maybe you would have held your fucking :ok_hand::ok_hand:shit. But you couldn’t, you didn’t, and now you’re paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You’re fucking dead, НO0ОଠOOOOOОଠଠOoooᵒᵒᵒᵒᵒᵒᵒᵒᵒ:ok_hand: :ok_hand::ok_hand: :ok_hand: :100: :ok_hand: :eyes: :eyes: .")
    
    responses.extend(response)

def whom_st_d_ve(discord, reddit, responses, message, channel):
    response = "whomst'd've'lu'yaint'nt'ed'ies's'y'es'nt't're'ing'able'tic'ive'al'nt'ne'm'll'ble'al'ny'less'w'ck'k'ly'py'nd'idy'ety'st'ged'ful'ish'ng'mt'ous'path'let'phile'like'ious'ant'script'ance'iatric'ite'emia'ory'age'ian'phone'ism'arium'ac'fy'ology'ure'pnea'ency'opia'loger'plegia'sophic'ent'hood'otomy'ward'ectomy'algia'orium'tude'cule'scribe'ization'crat'ade'gonic'onym'dom'ship'ic'ical'ial'ize'dox'itis'uous'scope'cycle'osis'ible'ular'acity'etic'cide'ative'plegic'ware'ese'ocity'sion'phyte'trophy'oma'ary'tome'scopy'ily'sect'ern'ist'esque'some'logist'phobia'iasis'pathy'ostomy'ling'ment'opsy'ee'oid'gam'gamy'cracy'ate'ine'oholic'aholic'escence'wise'arian'est'ness'eer'sophy'ette"
    
    responses.append(response)

def fffff(discord, reddit, responses, message, channel):
    response = 'f' if random.random() < .5 else 'F'
    
    if random.random() < .2:
        response *= random.randrange(2,11)
    
    responses.append(response)

def ive_never_bean_more_ashamed(discord, reddit, responses, message, channel):
    response = 'R' + 'E'*999
    responses.append(response)

#rule syntax: (function, regex search, channel blacklist, channel whitelist)
#channel blacklist and whitelist should be tuples
#leave channel whitelist empty or missing to disable

PUNCT_RE = "[!\"#\$%&'\\(\\)\*\\+,\\\\\\-\\.\\/:;<=>\\?@\\[\\]\\^_`{\\|}~\\s]"

command_rules = (
    (get_meme, "^! ?get(?:meme|mee+m|maymay)"),
    (get_porn, "^! ?getporn", ("general",)),
    (get_keem, "^! ?getkeem"),
    (get_dick, "^! ?getdick"),
    (get_furry_porn, "^! ?getfurryporn", ("general",)),
)

general_rules = (
    (joy_spam, "😂"),
    (right_there, "right there"),
    (hello_faggot, "hello!"),
    (boi_spam, "boi"),
    (high_noon, "what(?: (?:time'?s|time is) it|(?:'?s| is) the time)\\?"),
    (kkk_did_nothing_wrong, '.'),
    (nice_meme, '.', (), ("m3m3z",)),
    (shit_automod, "shit automod"),
    (whom_st_d_ve, "whom"),
    (fffff, "press f"),
)

#for deletion rules, the channel blacklist contains the names of all
#channels for which the rule DOES NOT apply

deletion_rules = (
    (ive_never_bean_more_ashamed, "(?:[b8]{0}*)+(?:[e3]{0}*)+(?:[a4]{0}*)+(?:[n]{0}*)+".format(PUNCT_RE), ("spicy-facebook-memes",)),
)
