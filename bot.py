from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Замініть 'YOUR_BOT_TOKEN' на реальний токен свого бота
TOKEN = 'YOUR_BOT_TOKEN'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Ви підписалися на найкращого бота! Не використовуйте команду "/stop"!!!😃')

def menu(update: Update, context: CallbackContext) -> None:
    menu_text = (
        "🎉 Привіт від 'CIS'! 🌟\n"
        "🚀Вітаємо у світі 3D та творчості! Знаємо, як зробити ваші ідеї реальністю.\n"
        "🌐Ми працюємо у 43 країнах, і тут готові вам допомогти!\n"
        "💬 Якщо є питання чи потрібна підтримка, пишіть нам.\n"
        "🌈✨Разом створюємо майбутнє! 🌈✨"
    )
    update.message.reply_text(menu_text)

def courses(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Записатися на курси до Віталіка.")
    context.user_data['waiting_for_name'] = True

def handle_text(update: Update, context: CallbackContext) -> None:
    text = update.message.text
    if context.user_data.get('waiting_for_name', False):
        context.user_data['name'] = text
        update.message.reply_text("Тепер введіть номер телефону.")
        context.user_data['waiting_for_name'] = False
        context.user_data['waiting_for_phone'] = True
    elif context.user_data.get('waiting_for_phone', False):
        phone_number = text
        update.message.reply_text(f"Дякуємо, {context.user_data['name']}! Ви записані на курси до Віталіка. Телефон: {phone_number}")

def lucky_test(update: Update, context: CallbackContext) -> None:
    import random
    lucky = random.choice([True, False])
    if lucky:
        update.message.reply_text("Везучі!")
    else:
        update.message.reply_text("Невезучі")

def main() -> None:
    updater = Updater(TOKEN)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("menu", menu))
    dp.add_handler(CommandHandler("courses", courses))
    dp.add_handler(CommandHandler("lucky_test", lucky_test))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_text))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
