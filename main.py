import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📘 Facebook Tools", callback_data="facebook")],
        [InlineKeyboardButton("📷 Instagram Tools", callback_data="instagram")],
        [InlineKeyboardButton("👤 Imposter Report", callback_data="imposter")]
    ]
    await update.message.reply_text(
        "Welcome to Restricted Force BD Bot",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "facebook":
        await query.edit_message_text(
            "Facebook Report Links:\nhttps://www.facebook.com/help/contact/295309487309948"
        )
    elif query.data == "instagram":
        await query.edit_message_text(
            "Instagram Report Links:\nhttps://help.instagram.com/"
        )
    elif query.data == "imposter":
        await query.edit_message_text(
            "Imposter Report Guide:\nUpload your ID and explain the account is impersonating you."
        )

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

app.run_polling()
