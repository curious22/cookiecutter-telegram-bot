from loguru import logger
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from src import configs


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


def main() -> None:
    app = ApplicationBuilder().token(configs.BOT_TOKEN).build()
    app.add_handler(CommandHandler('hello', hello))
    logger.debug('Bot has started')
    app.run_polling()
