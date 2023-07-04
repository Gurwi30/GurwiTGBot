from dotenv import load_dotenv;
from telegram import Update;
from telegram.ext import Application;
from commands.CMDHandler import loadCommands;
from inline.InlineHandler import loadInlineQueryHandler;
import os

def start_bot():
    bot: Application = Application.builder().token(os.getenv("TOKEN")).build();

    loadInlineQueryHandler(bot);
    bot.run_polling(allowed_updates=Update.ALL_TYPES);    

if __name__ == '__main__':
    load_dotenv();
    start_bot();