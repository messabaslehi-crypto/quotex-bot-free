import os
import traceback
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("TELEGRAM_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("اهلا! البوت شغال ✅")

def main():
    try:
        if not TOKEN:
            raise ValueError("TELEGRAM_TOKEN غير موجود في Environment Variables!")
        
        print(f"التوكن موجود: {TOKEN[:10]}...")
        app = Application.builder().token(TOKEN).build()
        app.add_handler(CommandHandler("start", start))
        print("البوت اشتغل...")
        app.run_polling(allowed_updates=Update.ALL_TYPES)
    
    except Exception as e:
        print("خطأ فادح:")
        traceback.print_exc()

if __name__ == "__main__":
    main()
