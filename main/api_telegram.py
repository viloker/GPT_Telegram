import logging
from telegram import Update
from telegram.ext import ContextTypes

from .api_openai import get_gpt_text, get_gpt_image

TOKEN = 'Your token for bot'

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    username = update.effective_chat.username
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'You are welcome {username}')


async def get_gpt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = get_gpt_text(update.message.text)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)


async def generation_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Bot work with you prompt")
    image_url = get_gpt_image(update.message.text[6::])
    await context.bot.send_message(chat_id=update.effective_chat.id, text=image_url)

