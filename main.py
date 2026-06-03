import asyncio
import os
import threading
from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

app = Flask(__name__)
TOKEN = os.environ.get('TELEGRAM_TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('البوت شغال 24 ساعة ✅')

def run_bot():
    print(f"التوكن موجود: {TOKEN[:10] if TOKEN else 'مفقود'}...")
    if not TOKEN:
        print("خطأ: حط التوكن في Environment")
        return
    
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    print("البوت اشتغل...")
    application.run_polling()

@app.route('/')
def home():
    return "البوت شغال ✅"

if __name__ == '__main__':
    # نشغل البوت في Thread لحاله
    threading.Thread(target=run_bot, daemon=True).start()
    # نشغل Flask عشان Render ما يطفي السيرفر
    app.run(host='0.0.0.0', port=10000)
