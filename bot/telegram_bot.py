import time

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

from services.layout_service import apply_layout
from config.settings import TELEGRAM_TOKEN, ALLOWED_USER_ID
from actions.executor import run_command

from ai.intent_parser import parse_intent

def is_allowed(user_id: int) -> bool:
    # cuma gua
    return user_id == ALLOWED_USER_ID

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # cek id
    user_id = update.effective_user.id
    
    if not is_allowed(user_id):
        await update.message.reply_text("Access denied.")
        return
    
    # ambil dan parse
    text = update.message.text
    tasks = parse_intent(text)

    if not tasks:
        await update.message.reply_text(
            "Gua gak ngerti 😭"
        )
        return
    
    results = []
    # run
    for task in tasks:
        result = run_command(task["command"])
        time.sleep(2) # biar sabar
        results.append(result)


        # abis run atur layout
        if task["layout"]:
            apply_layout(
                task["command"],
                task["layout"]
            )
        time.sleep(2) # biar sabar

    await update.message.reply_text("\n".join(results))


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