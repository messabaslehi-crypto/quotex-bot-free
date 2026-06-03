import os
import threading
import time
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

app = Flask(__name__)
TOKEN = os.getenv('TELEGRAM_TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('مرحبا! البوت شغال 24 ساعة ✅\nارسل اي رسالة')

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'وصلتني رسالتك: {update.message.text}')

def run_telegram_bot():
    print("="*40)
    print(f"TOKEN موجود: {'نعم' if TOKEN else 'لا'}")
    if TOKEN:
        print(f"اول 10 ارقام: {TOKEN[:10]}...")
    print("="*40)
    
    if not TOKEN:
        print("خطأ: ما لقيت التوكن! روح Environment في Render وحطه")
        return
    
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
    print("البوت بدأ يشتغل الان...")
    application.run_polling(drop_pending_updates=True)

@app.route('/')
def home():
    return "البوت شغال ✅ السيرفر حي"

if __name__ == '__main__':
    # نشغل البوت في Thread لحاله
    bot_thread = threading.Thread(target=run_telegram_bot, daemon=True)
    bot_thread.start()
    
    # نخلي Flask شغال عشان Render ما يطفي السيرفر
    app.run(host='0.0.0.0', port=10000)
