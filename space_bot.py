import os
from dotenv import load_dotenv
import telegram
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


# def hello(update: Update, context: CallbackContext) -> None:
#     update.message.reply_text(
#         f"Hello {update.effective_user.first_name}"
#     )


def main():

    load_dotenv()
    bot_token = os.getenv("BOT_TOKEN")
    chat_id="@myspacephotos"

    # updater = Updater(bot_token)
    # updater.dispatcher.add_handler(CommandHandler("hello", hello))
    # updater.start_polling()
    # updater.idle()
    
    bot = telegram.Bot(token=bot_token)
    # bot.send_message(
    #     chat_id="@myspacephotos",
    #     text="Hello world"
    # )
    bot.send_document(chat_id=chat_id, document=open('tests/test.png', 'rb'))


if __name__=="__main__":
    main()