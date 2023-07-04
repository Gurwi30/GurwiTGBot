from telegram import Update, InlineQueryResultArticle, InputTextMessageContent;
from telegram.constants import ParseMode;
from telegram.ext import Application, InlineQueryHandler, ContextTypes;
from html import escape
from uuid import uuid4

def loadInlineQueryHandler(bot: Application):
    bot.add_handler(InlineQueryHandler(inline_query));
    print(f"| Successfully loaded InlineQueryHandler");

async def inline_query(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.inline_query.query;
    if not query: return;

    results = [
        InlineQueryResultArticle(
            id=str(uuid4()),
            title="🛎️ Salva un promemoria",
            input_message_content=InputTextMessageContent(f"<b>🛎️ | PROMEMORIA SALVATO</b>\n👀 | {query}", ParseMode.HTML),
        ),
    ]

    await update.inline_query.answer(results)