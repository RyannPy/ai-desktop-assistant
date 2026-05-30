from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

from config.settings import TELEGRAM_TOKEN, ALLOWED_USER_ID
from commands.executor import run_command

from ai.intent_parser import parse_intent

def is_allowed(user_id: int) -> bool:
    return user_id == ALLOWED_USER_ID

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    
    if not is_allowed(user_id):
        await update.message.reply_text("Access denied.")
        return
    
    text = update.message.text
    intent = parse_intent(text)

    if not intent:
        await update.message.reply_text("Sorry, gua gak paham. Coba perintah lain.")
        return
    
    result = run_command(intent)
    await update.message.reply_text(result)


def start_bot():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", lambda update, context: update.message.reply_text("Halo! Mau dibukain apa hari ini?")))

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            handle_message
        )
    )
    
    print("Bot running..")

    app.run_polling()