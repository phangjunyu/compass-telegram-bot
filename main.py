# import pymongo
import os
import logging
from telegram.ext import CommandHandler, MessageHandler, Updater, Filters, PicklePersistence

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

def start(update, context):
    id = update.message.chat_id
    context.bot.send_message(chat_id=id, text="We sometimes get put down, feel defeated or stray off the path. Compass Bot is a bot that will store all your favourite personal quotes that you use to motivate yourself and echo it back to you at specific intervals, keeping you focused, committed and strongly certain on your path.")
    context.user_id = id
    # check if id is registered in DB
    # if registered, carry on, else create new instance in DB

def store(update, context):
    _tostore = update.message.text
    #stores message under the id in DB
    update.message.reply_text("Done!") # if successful

def retrieve_from_db(id):
    # function to call when timer is triggered
    # access db with id
    # randomly pick a quote
    result = None
    return result

def set_interval(update, context):
    id = update.message.chat_id
    # to specify time intervals
    # this should set a timer to repeat infinitely
    quote = retrieve_from_db(id)
    update.message.reply_text(quote)

def retrieve_all_quotes(id):
    #access db with id
    #returns formatted list of all quotes
    quotes = []
    return quotes

def edit_quote(update, context):
    retrieve_all_quotes(id)
    #first send all quotes


# this command must always be the last command added
def unknown(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")

def main():
    # client = pymongo.MongoClient("mongodb+srv://phangjunyu:<password>@cluster0-flkcn.mongodb.net/test?retryWrites=true&w=majority")
    # db = client.test
    token=""
    pp = PicklePersistence(filename='compassbot_chatid')
    updater = Updater(token=token, persistence=pp, use_context=True)
    # updater = Updater(token=os.environ.get('TelegramAPI'), use_context=True)
    dp = updater.dispatcher
    unknown_handler = MessageHandler(Filters.command, unknown)
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('store', store))
    dp.add_handler(CommandHandler('edit', edit_quote))
    dp.add_handler(unknown_handler)

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()