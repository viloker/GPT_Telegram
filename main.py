from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from main.api_telegram import TOKEN, start, get_gpt, generation_image

def main():
    application = ApplicationBuilder().token(TOKEN).build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    gpt_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), get_gpt)
    application.add_handler(gpt_handler)

    image_handler = CommandHandler('image', generation_image)
    application.add_handler(image_handler)


    application.run_polling()


if __name__ == '__main__':
    main()