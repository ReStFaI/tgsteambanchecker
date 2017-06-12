import requests, json, telegram, time

# SETTINGS
bot = telegram.Bot(token='BOT_TOKEN')  #Telegram bot token
apikey = "KEY" #Steam Web Api Key
chat_id = USERID #ID of Telegram user to whom data will be sent. You can get it by @ShowJsonBot 
# SETTINGS

steam_ids = []
with open('ids.txt') as f:
    steam_ids = f.read().splitlines()
print (steam_ids)
f.close()

vac = 0
ow = 0

def ReplaceLineInFile(fileName, sourceText, replaceText):
    file = open(fileName, 'r')
    text = file.read()
    file.close()
    file = open(fileName, 'w')
    file.write(text.replace(sourceText, replaceText))
    file.close()
    print 'Steamid removed from file successfuly'

for steam_id in steam_ids:
	r = requests.get(url=("http://api.steampowered.com/ISteamUser/GetPlayerBans/v1/?key=%s&steamids=%s" % (apikey, steam_id))) 
	parsed_string = json.loads(r.text) 
	vac = parsed_string['players'][0]['NumberOfVACBans'] 
	ow = parsed_string['players'][0]['NumberOfGameBans'] 
	if vac == 1 or ow == 1: 
		json_for_playersumm = requests.get(url=("http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=%s&steamids=%s" % (apikey, steam_id)))
		jsonload = json.loads(json_for_playersumm.text)
		username = jsonload['response']['players'][0]['personaname']
	
	if vac == 1:
		bot.send_message(chat_id=chat_id, text="Account was banned \nSteamID: %s\nUsername: %s\nBan type: VAC\nLink: steamcommunity.com/profiles/%s" % (steam_id, username, steam_id))
		time.sleep(1)
		ReplaceLineInFile('ids.txt', steam_id + '\n', '') 
		time.sleep(1)
		
	if ow == 1:
		bot.send_message(chat_id=chat_id, text="Account was banned \nSteamID: %s\nUsername: %s\nBan type: Overwatch\nLink: steamcommunity.com/profiles/%s" % (steam_id, username, steam_id))
		time.sleep(1)
		ReplaceLineInFile('ids.txt', steam_id + '\n', '') 
		time.sleep(1)
