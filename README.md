# Upload photos of space to Telegram
Automate the collection of space photos to publish them on Telegram.

## Usage
0. Create enviroment variables. See a topic "Create enviroment variable" for example.
1. Run `download_images.py` to download space photos.
```
python download_images.py
```
Folders `apod_images`, `epic_images`, `images` will be created.
![](https://github.com/vip-v2a/space_telegram/blob/ff70cc96f37b8323293d501f60e726e0db21d87b/ext/images.JPG)

2. Run `space_bot.py` to post photos once a day in Telegram group.
```
python space_bot.py
```
Then you see messages in Telegram group:
![](https://github.com/vip-v2a/space_telegram/blob/ff70cc96f37b8323293d501f60e726e0db21d87b/ext/space_bot.gif)

## Getting Started
### Prerequisites

You need create environment variables:
- `NASA_API_KEY` NASA API Token.
- `BOT_TOKEN` from @Bot_father.
- `DELAY` time delay between bot Telegram posts (default, 1 day). You can set new value if you need another time period.
- `CHAT_ID` chat id Telegram group where bot was added (example, "@groupname").

If you need [creation of virtual environment](https://vc.ru/dev/240211-nastroyka-rabochego-okruzheniya-na-windows-dlya-raboty-s-python).

You need install `requirements.txt`:
```    
pip install -r requirements.txt
```

### Get `NASA_API_KEY`
- Go to [NASA APIs](https://api.nasa.gov/).
- Click "Generate API Key" on top menu.
- Type required fields.
- Copy your API key.

### Create enviroment variable
Type command in Command Prompt:
```
set NASA_API_KEY=your-API-key-here
set BOT_TOKEN=your-bot-API-token
set DELAY=your-new-time-delay-ms
set CHAT_ID=@tggroupname
```

### python-telegram-bot documentation
[Getting started.](https://python-telegram-bot.org/)

[How to create channel with bot.](https://smmplanner.com/blog/otlozhennyj-posting-v-telegram/)

[python-telegram-bot. Pure API. Snippets.](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Code-snippets#working-with-files-and-media)

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
