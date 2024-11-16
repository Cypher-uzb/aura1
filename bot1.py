import os
import subprocess
import sys

# Kutubxona mavjudligini tekshirish va o'rnatish
try:
    from telegram import Update
    from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
except ImportError:
    print("Zarur kutubxonalar yo'q. Ularni o'rnatish boshlandi...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
    subprocess.check_call([sys.executable, "-m", "pip", "install", "python-telegram-bot"])
    print("Kutubxonalar muvaffaqiyatli o'rnatildi. Dastur qaytadan ishga tushirilmoqda...")
    os.execl(sys.executable, sys.executable, *sys.argv)

# Bot funksiyalari
async def start(update: Update, context):
    await update.message.reply_text("Assalomu alaykum! Men Telegram botman! Menga biror narsa yozing, men sizga qaytarib yuboraman.")

async def echo(update: Update, context):
    user_message = update.message.text
    await update.message.reply_text(f"Siz yubordingiz: {user_message}")

# Asosiy funksiya
if __name__ == "__main__":
    BOT_TOKEN = "7635357748:AAHDO2KSlDIqVhkRZUcW51vzEXi8Mf2XuRg"  # BotFather dan olingan tokenni bu yerga kiriting
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # Handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Botni ishga tushirish
    print("Bot ishga tushdi. Telegramda uni sinab ko'ring!")
    application.run_polling()
