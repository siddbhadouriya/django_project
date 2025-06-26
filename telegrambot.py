import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangojwt.settings')
django.setup()


from telegram import Update
from myapp.models import *
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters


API_KEY = "8111119919:AAE8aNBBD5B5HvlB7kX5ZolxUki64qaEGfY"  # ← yahan apna actual token daalo
  # ← apna actual Telegram API key daaliye

# Handler function
async def handle_message(update, context):
    if update.message:
        user_first_name = update.message.chat.first_name
        await update.message.reply_text(f"Hi! I am Sidd: {user_first_name}")


# Main app setup
if __name__ == '__main__':
    app = ApplicationBuilder().token(API_KEY).build()

    # Add message handler (ignores commands like /start)
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))

    print("🤖 Telegram bot is running...")
    app.run_polling()

