from telegram.ext import Updater,CommandHandler,MessageHandler,Filters
from telegram import ChatAction
from db_interact import show_all,insert_task,search_tuple,delete_task

def start(bot,update):
    update.message.reply_text("Hey! I'm here to help you keep track of your to do :)")

def echo_err(bot,update):
    bot.sendChatAction(update.message.chat_id,ChatAction.TYPING)
    update.message.reply_text("I'm sorry, I can only understand commands...")

def showTasks(bot,update):
    bot.sendChatAction(update.message.chat_id,ChatAction.TYPING)
    result = show_all()
    update.message.reply_text(result)

def newTask(bot,update, args):
    if not args:
        update.message.reply_text("Insert a task to add!")
    else:
        task = " ".join(args)
        bot.sendChatAction(update.message.chat_id,ChatAction.TYPING)
        insert_task(task)
        update.message.reply_text("Task successfully added!")

def removeTask(bot,update,args):
    task = " ".join(args)
    if search_tuple(task):
        update.message.reply_text("The task was successfully deleted!")
        delete_task(task)
    else:
        update.message.reply_text("The task you specified is not in the list!")

def main():
    # create the EventHandler
    updater = Updater("899776756:AAEWPf7VbJLCi6EgygUa8Tp9YVztocIsQyc")
    # get the dispacer to register handlers
    dp = updater.dispatcher

    # add handler for the start command
    dp.add_handler(CommandHandler("start", start))
    # add handler for "/showTasks
    dp.add_handler(CommandHandler("showTasks", showTasks))
    # add handler for "/newTask"
    dp.add_handler(CommandHandler("newTask", newTask, pass_args=True))
    # add handler for "/removeTask"
    dp.add_handler(CommandHandler("removeTask", removeTask, pass_args=True))
    # add handler for "/removeAllTasks"
    #dp.add_handler(CommandHandler("removeAllTasks", removeAllTasks, pass_args=True))
    # on non-command textual messages - echo error message
    dp.add_handler(MessageHandler(Filters.text, echo_err))

    # start the bot
    updater.start_polling()
    # loop the bot
    updater.idle()

if __name__ == '__main__':
    main()