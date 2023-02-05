import logging
from dotenv import dotenv_values

from telegram import (
    Update,
    ForceReply,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ParseMode,
)
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackContext,
    CallbackQueryHandler,
)

# Returns a dictonary with all the .env key and value pairs:
config = dotenv_values(".env")
API_KEY = config["TELEGRAM_API_KEY"]

logger = logging.getLogger(__name__)

# Bot screaming status:
screaming = False
