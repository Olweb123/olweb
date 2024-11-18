import openai
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Укажите ключи
TELEGRAM_TOKEN = "7464784797:AAG1drM6Jq4fMQepWqXrZnOqfQ5sGflq2jA"
OPENAI_API_KEY = "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"

openai.api_key = OPENAI_API_KEY

# Обработка сообщений
def handle_message(update: Update, context: CallbackContext):
    user_message = update.message.text
    chat_id = update.message.chat_id
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": user_message}],
        )
        bot_reply = response['choices'][0]['message']['content']
    except Exception as e:
        bot_reply = "Произошла ошибка: " + str(e)
    context.bot.send_message(chat_id=chat_id, text=bot_reply)

# Команда /start
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Салам бродяга. Я наркодырский бля бот GPT. Напиши мне что-нибудь, только не просит у меня 100 рублей!")

# Основная функция
def main():
    updater = Updater(TELEGRAM_TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    updater.start_polling()
    updater.idle()

if name == "__main__":
    main()
