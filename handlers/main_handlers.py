from aiogram import Dispatcher
from aiogram.types import KeyboardButton, Message, ReplyKeyboardMarkup

from data_base.db_functions import get_moderator_id
from texts.buttons import BUTTONS
from texts.commands import COMMANDS
from texts.messages import MESSAGES


def get_main_keyboard(is_moderator=False):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    my_projects_button = KeyboardButton(BUTTONS["sell_menu"])
    search_projects_button = KeyboardButton(BUTTONS["buy_menu"])
    information_button = KeyboardButton(BUTTONS["information"])
    if is_moderator:
        moderator_button = KeyboardButton(BUTTONS["moderate"])
        markup.add(my_projects_button, search_projects_button, information_button, moderator_button)
    else:
        markup.add(my_projects_button, search_projects_button, information_button)
    return markup


async def start_command(message: Message):
    await main_menu(message, message_text=MESSAGES["start"].format(message.from_user))


async def back_by_button(message: Message):
    await main_menu(message, message_text=MESSAGES["main_menu"])


async def back_by_command(message: Message):
    await main_menu(message, message_text=MESSAGES["main_menu"])


async def main_menu(message, message_text):
    is_moderator = False
    if message.from_user.id == get_moderator_id():
        is_moderator = True
    await message.answer(
        text=message_text,
        reply_markup=get_main_keyboard(is_moderator=is_moderator),
    )


def register_main_handlers(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=[COMMANDS["start"]])
    dp.register_message_handler(back_by_button, text=[BUTTONS["back"]])
    dp.register_message_handler(back_by_command, commands=[COMMANDS["back"]])
