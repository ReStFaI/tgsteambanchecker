# Installation
#### Linux
1. Install Python 2.7 & pip
2. Download repository:
```
git clone https://github.com/BoberMod/tgsteambanchecker.git
cd tgsteambanchecker
```
3. Install all dependencies:
```
pip install -r requirements.txt
```
6. Edit ```bot.py```
```
# SETTINGS
bot = telegram.Bot(token='BOT_TOKEN')  #Telegram bot token (Create bot by @BotFather)
apikey = "KEY" #Steam Web Api Key https://steamcommunity.com/dev/apikey
chat_id = USERID #ID of Telegram user to whom data will be sent. You can get it by @ShowJsonBot 
# SETTINGS
```
5. Edit ```ids.txt```.
Each steamID must start with a new line. 
At the end there must be an empty string.
6. Edit start.sh
```
sleep 1m - delay (in minutes)
```
7. Run start.sh

