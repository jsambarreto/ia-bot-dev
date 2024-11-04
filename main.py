import telebot # type: ignore
import openai  # type: ignore
import os
from dotenv import load_dotenv # type: ignore

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Obtém as variáveis de ambiente
api_key = os.getenv('API_KEY')
base_url = os.getenv('BASE_URL')

# Cria o cliente da LLM
client = openai.OpenAI(
    api_key=api_key,
    base_url=base_url,
)

# Cria o bot do Telegram
token_bot = os.getenv('TOKEN_BOT')
bot = telebot.TeleBot(token_bot, parse_mode=None)#telegram.Bot(token_bot)

def handle_messages(messages):
	for message in messages:
		response = client.chat.completions.create(
			model="sabia-2-small",
			messages=[
				{"role": "system", "content": """Você é o RoboJorgeDev, robô de desenvolvimento para testes"""},
				{"role": "user", "content": message.text},
				],
			#max_tokens=8000
			)
		bot.reply_to(message, response.choices[0].message.content)

bot.set_update_listener(handle_messages)
bot.infinity_polling()

