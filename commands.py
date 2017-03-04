import re #eeeeee

#rule syntax: (function, regex search, channel blacklist, channel whitelist)
#channel blacklist and whitelist should be tuples
#leave channel whitelist empty to disable

command_rules = (
(get_dick, "^!getdick"),
(get_keem, "^!getkeem"),
(get_meme, "^!getmeme"),
(get_porn, "^!getporn", ("general"))
)

general_rules = (
(joy_spam, "😂"),
(right_there, "right there"),
(hello_faggot, "hello!"),
(boi_spam, "boi"),
(high_noon, "what(?: (?:time'?s|time is) it|(?:'?s| is) the time)\?")
)

def on_message(client, message, channel):
    def good_channel(rule, channel):
        return (channel not in rule[2]) and ((not rule[3]) or (channel in rule[3]))
    
    def re_evaluate(exp, body):
        return re.search(exp, body, re.IGNORECASE) is not None
    
    body = message.content
    
    for rule in command_rules:
        if good_channel(rule, channel) and re_evaluate(rule[1], body):
            rule[0](client, message, channel)
            break
            
    for rule in general_rules:
        if good_channel(rule, channel) and re_evaluate(rule[1], body):
            rule[0](client, message, channel)

# Command Definitons

def get_dick(client, message, channel):
    pass #Fin can do this I guess

# General Response Definitons

def joy_spam(client, message, channel):
    response = (':joy:'*400).format(message)
    await client.send_message(channel, response)

def right_there(client, message, channel):
    response = ":ok_hand::ok_hand::ok_hand: right:heavy_check_mark:there :heavy_check_mark::heavy_check_mark:if i do ƽaү so my self :100: i say so :100: thats what im talking about right there right there (chorus: ʳᶦᵍʰᵗ ᵗʰᵉʳᵉ) mMMMMᎷМ:100: :ok_hand::ok_hand: :ok_hand:НO0ОଠOOOOOОଠଠOoooᵒᵒᵒᵒᵒᵒᵒᵒᵒ:ok_hand: :ok_hand::ok_hand: :ok_hand: :100: :ok_hand: :eyes: :eyes: :eyes: :ok_hand::ok_hand:Good shit"
    
    await client.send_message(channel, response)

def hello_faggot(client, message, channel):
    response = "Fuck you faggot"
    await client.send_message(channel, response)

def boi_spam(client, message, channel):
    response = 'i'*1000
    await client.send_message(channel, response)

def high_noon(client, message, channel):
    response = "It's high noon!"
    await client.send_message(channel, response)
