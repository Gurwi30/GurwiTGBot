from commands.CMDHandler import Update, ContextTypes;

async def executer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Scroto");