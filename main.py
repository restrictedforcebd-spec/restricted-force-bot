from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = "YOUR_BOT_TOKEN"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🛡️ Welcome to Restricted Force BD Bot!\n\n"
        "এই বটে শীঘ্রই Facebook ও Instagram Tools যোগ করা হবে।"
    )

app = Application.builder().token(8996305727:AAHoeTWpjmPgntFRdu8uX7DoVi_HDKHRT9I).build()
app.add_handler(CommandHandler("start", start))

print("Bot is running...")
app.run_polling()
