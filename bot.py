from telegram.ext import *
from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import create_db

TOKEN: Final = "6019560557:AAEI-4WB7g4BR87kX5yG7F7vvB5Sy3-GVS0"
BOT_USERNAME: Final = "@KatsaBot"


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('type something random to  get started')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("help")
    await update.message.reply_text('help')


async def projects_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("projects")
    projects = create_db.projects_query()
    message = ""
    for project in projects:
        message += "Name: " + str(project['name']) + " id: " + str(project['id']) + "\n"
    print(message)
    await update.message.reply_text('projects list: \n' + message)


async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('custom')






def handle_response(text: str) -> str:
    # Create your own response logic
    processed: str = text.lower()

    if 'project' in processed:
        print(1)
        projects = create_db.projects_query()
        id = processed.split(' ')[1]
        project=[ pro for pro in projects if int(pro['id'])==int(id)]
       # project = filter(lambda pro: pro['id'] == id, projects)
       #  print([ pro for pro in projects if int(pro['id'])==int(id)])
        message="פרטי הפרוייקט שבחרת הם: \n"+f"שם הפרוייקט:{project[0]['name']}"+"\n"+f"שם פקח: {project[0]['supervisorName']}"+"\n"+f"מיקום:{project[0]['location']}" +"\n"
        return message

    # if 'how are you' in processed:
    #     return 'I\'m good!'
    #
    # if 'i love python' in processed:
    #     return 'Remember to subscribe!'

    return 'I don\'t understand'


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text
    print(f'user ({update.message.chat_id}) in {message_type}:"{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)
    print('bot mm', response)
    await update.message.reply_text(response)


if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('projects', projects_command))
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    app.run_polling(poll_interval=3)

# def help_command(update, context):
#     update.message.reply_text('if you need help: you sjuld ask google')
#
#
# def handle_command(update, context):
#     text = str(update.message.text).lower()
#     update.message.reply_text("nadav the king" + text)
#
#
# def main():
#     updater = Updater(Token, use)
#     dp =updater
#
#
#     dp.
