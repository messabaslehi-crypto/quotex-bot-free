import os
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("TELEGRAM_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("اهلا! البوت شغال 100% ✅")

async def main():
    if not TOKEN:
        print("خطأ: TELEGRAM_TOKEN غير موجود!")
        return
    
    print(f"التوكن موجود: {TOKEN[:10]}...")
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("البوت اشتغل...")
    
    await app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    asyncio.run(main())
