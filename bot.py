from telegram import *
from telegram.ext import *

token = '__API__KEY__'
bot = Bot(token=token)
def hey(update: Update, context: CallbackContext):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text='yooooo <3'
        )

def start(update: Update, context: CallbackContext):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text='Hey '+ update.effective_user.full_name + ' lets get into it'
        )

def __main__():
    updt = Updater(token, use_context=True)
    dispatcher = updt.dispatcher
    comm1 = CommandHandler('hey', hey)
    comm2 = CommandHandler('start', start)
    dispatcher.add_handler(comm1)
    dispatcher.add_handler(comm2)
    updt.start_polling(poll_interval=0, timeout=30)
    
    #print(bot.get_me())

if __name__ == '__main__':
    __main__()