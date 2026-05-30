from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from config.settings import TELEGRAM_TOKEN, ALLOWED_USER_ID
from commands.executor import run_command

def is_allowed(user_id: int):
    return user_id in ALLOWED_USER_ID

async def handle_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if not is_allowed(user_id):
        await update.message.reply_text("Access denied.")
        return
    
    cmd = update.message.text.replace("/ ", "").strip()

    result = run_command(cmd)
    await update.message.reply_text(result)

def start_bot():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("vscode", handle_command))
    app.add_handler(CommandHandler("chrome", handle_command))
    app.add_handler(CommandHandler("notepad", handle_command))
    print("Bot running..")

    app.run_polling()