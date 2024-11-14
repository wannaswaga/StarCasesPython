from telegram import LabeledPrice, Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, PreCheckoutQueryHandler, MessageHandler, filters, ContextTypes

# Функция для отправки инвойса на пополнение
async def send_invoice(update: Update, context: ContextTypes.DEFAULT_TYPE, amount: int):
    prices = [LabeledPrice(label="Оплата Stars", amount=amount * 100)]
    await update.message.reply_invoice(
        title="Пополнение Stars",
        description="Пополнение для открытия кейсов.",
        payload="purchase_stars",
        provider_token="YOUR_PROVIDER_TOKEN",  # Вставьте токен провайдера
        currency="XTR",
        prices=prices
    )

async def pre_checkout_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.pre_checkout_query
    await query.answer(ok=True)

async def successful_payment_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Платеж успешно завершен! Ваш баланс пополнен.")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("Открыть Казино", web_app=WebAppInfo(url="https://legendary-halva-2731c4.netlify.app"))]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Нажмите на кнопку ниже, чтобы открыть Казино.", reply_markup=reply_markup)

def main():
    application = Application.builder().token("7703484036:AAHZIXT9xOgUwoA23xX4kTTVPM0Ek52F0Y0").build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("buy_stars", send_invoice))
    application.add_handler(PreCheckoutQueryHandler(pre_checkout_handler))
    application.add_handler(MessageHandler(filters.SUCCESSFUL_PAYMENT, successful_payment_handler))
    application.run_polling()

if __name__ == "__main__":
    main()
