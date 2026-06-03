import time

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from telegram.constants import ChatAction

from services.layout_service import apply_layout
from services.desktop_service import switch_to_desktop

from config.settings import TELEGRAM_TOKEN, ALLOWED_USER_ID
from actions.executor import run_command

from ai.planner import ai_plan
from ai.responses import START_RESPONSES, UNKNOWN_RESPONSES, ACCESS_DENIED_RESPONSES, PLANNING_RESPONSES, SUCCESS_RESPONSES, pick

from services.loading_service import (
    create_loading_message,
    loading_step,
    delete_loading_message
)

def is_allowed(user_id: int) -> bool:
    # cuma gua
    return user_id == ALLOWED_USER_ID

async def start(update, context):
    await update.message.reply_text(
        pick(START_RESPONSES)
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # cek id
    user_id = update.effective_user.id
    
    if not is_allowed(user_id):
        await update.message.reply_text(pick(ACCESS_DENIED_RESPONSES))
        return
    
    # ambil
    text = update.message.text

    loading = await create_loading_message(
        update,
        "🧠 Memahami perintah..."
    )

    await context.bot.send_chat_action(
        chat_id=update.effective_chat.id,
        action=ChatAction.TYPING
    )
    
    # parsing & planning
    tasks = ai_plan(text)


    # loading
    await loading_step(
        loading,
        pick(PLANNING_RESPONSES),
    )
    
    if not tasks:
        await update.message.reply_text(
            pick(UNKNOWN_RESPONSES)
        )
        return
    
    results = []

    await loading_step(
        loading,
        "🖥️ Menjalankan task..."
    )
    # run
    for task in tasks:

        # atur desktop
        switch_to_desktop(task["desktop"])

        # run
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

    await delete_loading_message(
        loading
    )

    summary = "\n".join(results)

    await update.message.reply_text(
        f"{pick(SUCCESS_RESPONSES)}\n\n{summary}"
    )


def start_bot():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            handle_message
        )
    )
    
    print("Bot running..")

    app.run_polling()