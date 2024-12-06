import os
import logging
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from dotenv import load_dotenv

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message when the command /start is issued."""
    keyboard = [
        [
            ("Левая"),
            ("Правая"),
        ],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
    # await update.message.reply_text("Выберите кнопку:", reply_markup=reply_markup)


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Echo the user message."""
    button_text = update.message.text
    await update.message.reply_text(button_text)
    await update.message.reply_text("Какая сиська?:", reply_markup=ReplyKeyboardMarkup([
        [
            ("Левая"),
            ("Правая"),
        ],
    ], one_time_keyboard=True))


if __name__ == '__main__':
    load_dotenv()
    application = ApplicationBuilder().token(os.getenv("YOUR_BOT_TOKEN")).build()

    start_handler = CommandHandler('start', start)
    button_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, button)

    application.add_handler(start_handler)
    application.add_handler(button_handler)

    application.run_polling()
