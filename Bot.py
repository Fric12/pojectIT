from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

TOKEN = '6920885849:AAGGDOJbSuYXoBrRuMHHWzIH0GAODXcZUzI'

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
    update.message.reply_text("Оберіть курс для запису:", reply_markup=get_courses_keyboard())

def get_courses_keyboard():
    from telegram import ReplyKeyboardMarkup

    keyboard = [
        ["Записатися на курси до Віталіка.", "Записатися на курси до Данила."],
    ]

    return ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)

def handle_text(update: Update, context: CallbackContext) -> None:
    text = update.message.text
    if text == "Записатися на курси до Віталіка.":
        update.message.reply_text("Записатися на курси до Віталіка.")
        context.user_data['waiting_for_name'] = True
        context.user_data['course'] = 'Віталіка'
    elif text == "Записатися на курси до Данила.":
        update.message.reply_text("Записатися на курси до Данила.")
        context.user_data['waiting_for_name'] = True
        context.user_data['course'] = 'Данила'

def handle_name(update: Update, context: CallbackContext) -> None:
    name = update.message.text
    context.user_data['name'] = name
    update.message.reply_text("Тепер введіть номер телефону.")
    context.user_data['waiting_for_name'] = False
    context.user_data['waiting_for_phone'] = True

def handle_phone(update: Update, context: CallbackContext) -> None:
    phone_number = update.message.text
    course = context.user_data['course']
    name = context.user_data['name']
    update.message.reply_text(f"Дякуємо, {name}! Ви записані на курси до {course}. Телефон: {phone_number}")

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
    dp.add_handler(MessageHandler(Filters.regex("^(Записатися на курси до Віталіка.|Записатися на курси до Данила.)$"), courses))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command & Filters.regex("^(?!/).*"), handle_text))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command & Filters.regex("^(?!.*/).*"), handle_name))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command & Filters.regex("^(?!.*/).*"), handle_phone))
    dp.add_handler(CommandHandler("lucky_test", lucky_test))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
