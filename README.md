# Upload photos of space to Telegram
Automate the collection of space photos to publish them on Telegram.

## Example

## Getting Started
### Prerequisites

You need create environment variable:
- `NASA_API_KEY` NASA API Token.

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
```


### Deploy on Heroku
- Repository has `.Procfile` to deploy on Heroku.
- Logs are printed into Telegram (`TELEGRAM_ID`).

To deploy on [Heroku](https://heroku.com/): 
- create a new app on European server.
- create Reveal Config Vars from 'Settings' tab (How to generate a Google credential see below). 
- open 'Deploy' tab on the top menu.
- connect to your github profile.
- select your bots repository.
- choose a branch to deploy 'master' .
- press 'Deploy Branch'.
- waiting 'Your app was successfully deployed'.
- go to 'Recources' tab.
- turn on dynos (if need, edit dino formation -> then switch ON dino app -> confirm).
- drink a cup of tea)
