import os
import smtplib
from email.mime.text import MIMEText

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    MessageHandler,
    ContextTypes,
    filters
)

TOKEN = os.getenv("8700820594:AAG2wz1a65QoDcSsOhfZtKRmnDqXozolW50")
EMAIL = os.getenv("jamessnderson27@gmail.com")
PASSWORD = os.getenv("vivi_333")
TUJUAN = os.getenv("support@support.whatsapp.com")

async def pesan(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text

    msg = MIMEText(text)

    msg["Compose email"] = "Pesan Telegram"
    msg["From"] = EMAIL
    msg["To"] = TUJUAN

    try:

        server = smtplib.SMTP(
            "smtp.gmail.com",
            587
        )

        server.starttls()

        server.login(
            EMAIL,
            PASSWORD
        )

        server.send_message(msg)

        server.quit()

        await update.message.reply_text(
            "Terkirim!"
        )

    except Exception as e:

        await update.message.reply_text(
            str(e)
        )

app = (
    ApplicationBuilder()
    .token(TOKEN)
    .build()
)

app.add_handler(
    MessageHandler(
        filters.TEXT,
        pesan
    )
)

print("Bot hidup")

app.run_polling()
