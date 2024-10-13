
# GPT Telegram
Your personal ChatGPT in Telegram


## Clone the Project
Open a directory in Terminal where you want to clone the project and use one of the following commands:

#### HTTPS:
```
git clone https://github.com/viloker/GPT_Telegram.git
```

#### SSH:
```
git clone git@github.com:viloker/GPT_Telegram.git
```

## Create a Virtual Environment
To create a virtual environment, run:
```
python -m venv venv
```

Activate the virtual environment:

- **Windows:**
  ```
  venv\Scripts\activate
  ```

- **macOS/Linux:**
  ```
  source venv/bin/activate
  ```

## Install Dependencies
Run the following command to install all required packages:
```
pip install -r requirements.txt
```

### Or install manually:
```
pip install openai python-telegram-bot
```

## Get the Telegram API Token
Go to [BotFather](https://telegram.me/BotFather) and create your bot.
Once your bot is created, retrieve the **token** and add it to the `api_telegram.py` file:
```
TOKEN = 'Your token for the bot'
```

## Get the OpenAI API Key
Go to the [OpenAI API page](https://platform.openai.com/api-keys) and generate an API key.
Then, add your key to the `api_openai.py` file:
```
API = 'Your OpenAI API key'
```

### Note: 
<span style="color: #ff6666" >If your OpenAI account balance is 0, you will need to purchase additional credits (a minimum of $5 is required). </span>
## You're All Set!
Now you can start the bot by running the following command in the Terminal:
```
python main.py
```

## Example
#### How GPT gives you an answer
![Test GPT in Telegram](/example/chat_gpt_work.png)
#### How DALL·E 3 gives you an answer
![Test Dall-E 3 in Telegram](/example/dall_e_work.png)