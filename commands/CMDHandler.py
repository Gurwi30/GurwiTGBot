from telegram import Update;
from telegram.ext import Application, CommandHandler, ContextTypes;

from commands.HelpCommand import executer;

def loadCommands(bot: Application):
    registerCommand("help", executer, bot);

def registerCommand(name: str, func, bot: Application):
    bot.add_handler(CommandHandler(name, func));
    print(f"| Registered Command {name} successfully!");