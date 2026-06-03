import asyncio
import os
from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

app = Flask(__name__)
TOKEN = os.environ.get('TELEGRAM_TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('البوت شغال ✅ ارسل /start')

@app.route('/')
def home():
    return "البوت شغال 24 ساعة ✅"

async def main():
    if not TOKEN:
        print("خطأ: التوكن مفقود!")
        return
    
    print(f"التوكن موجود: {TOKEN[:10]}...")
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    
    # نشغل Flask في الخلفية
    loop = asyncio.get_event_loop()
    loop.run_in_executor(None, lambda: app.run(host='0.0.0.0', port=10000, use_reloader=False))
    
    # نشغل البوت
    await application.initialize()
    await application.start()
    await application.updater.start_polling()
    print("البوت اشتغل...")
    await application.updater.idle()

if __name__ == '__main__':
    asyncio.run(main())
