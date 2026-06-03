import asyncio


async def create_loading_message(update, text="Memahami perintah..."):
    """
    Buat pesan loading awal.
    """
    return await update.message.reply_text(text)


async def update_loading_message(message, text):
    """
    Update pesan loading yang sudah ada.
    """
    await message.edit_text(text)


async def delete_loading_message(message):
    """
    Hapus pesan loading.
    """
    await message.delete()


async def loading_step(message, text, delay=0):
    """
    Update loading + optional delay.
    """
    await update_loading_message(message, text)

    if delay > 0:
        await asyncio.sleep(delay)