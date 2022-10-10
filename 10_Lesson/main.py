from pytube import YouTube
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello (update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello  {update.effective_user.first_name}')

async def Download(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(' Напишите: /link ссылка')
    
    

async def Link1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global link
    stroka = update.message.text
    s = stroka.split()
    link = s[1]
    
    await update.message.reply_text('Выберите /video или /audio скачать')
    

async def Video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = YouTube(str(link))
    video = url.streams.first()
    video.download()
    

async def Audio(update: Update, context: ContextTypes.DEFAULT_TYPE, link):
    url = YouTube(str(link))
    audio = url.streams.filter(only_audio=True).desc().first()
    audio.download()


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('/hello\n/help\n/download')


    



app = ApplicationBuilder().token("5698321088:AAFFid2OJVXMyoNZWCZGZgruBpDv97jIVDo").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("download", Download))
app.add_handler(CommandHandler("link", Link1))
app.add_handler(CommandHandler("video", Video))
app.add_handler(CommandHandler("audio", Audio))
app.add_handler(CommandHandler("help", help))
print('server start')

app.run_polling()