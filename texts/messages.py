start_message = (
    "Здравствуйте, {0.first_name}! Я тестовый бот для продажи и покупки проектов!"
)

main_menu_massage = "📌 Главное меню 📌"

sell_menu_message = "🗄 Мои предложения 🗄"
put_up_for_sale_massage = "🖊Заполните анкету🖊"
project_name_question = "Напишите название вашего проекта:"
price_question = "Напишите цену вашего проекта"
price_check_question = "Цена должна быть числом. Напишите цену вашего проекта:"
subscribers_question = "Сколько подписчиков у вашего проекта?"
subscribers_check_question = "Укажите количество подписчиков числом. Напишите сколько подписчиков у вашего проекта:"
income_question = "Какой доход у вашего проекта?"
income_check_question = "Укажите доход проекта числом. Какой доход у вашего проекта:"
themes_question = "Выберете не более 3-х тематик вашего проекта:"
themes_warn_question = "Такой темы нет в списке! Выберите тему из списка"
themes_warn_2_question = "Данная тема уже добавлена!"
themes_plus_1_question = "Выберите ещё одну тему"
themes_plus_question = "Хотите выбрать ещё тему?"
yes_question = "Да"
no_question = "Нет"
comment_question = "Добавьте комментарий к обьявлению:"
confirm_question = (
    "Данные введены верно? Если да, то перейдите к оплате. "
    "При нажатии кнопки 'Отмена' Вы вернётесь в главное меню.\n\n"
    "<b>Название:</b> {name}\n<b>Тематика:</b> {themes}\n<b>Подписчиков:</b> {subs}\n<b>Доход в "
    "месяц:</b> {income}\n\n<b>Комментарий:</b> {comm}\n\n<b>Продавец:</b> @{"
    "seller}\n\n<b>Цена:</b> {price}"
)
payment_message = "Начинается процесс оплаты"

cancellation_question = "Отмена"
save_project_question = "Ваше обьявление сохранено!"

get_list_of_projects_message = "🗄 Выставленные на продажу предложения 🗄"

buy_menu_message = "💰 Поиск предложений 💰"
chose_themes_message = "Выберите интересные тематики"
chose_price_from_message = "Введите цену от: "
chose_price_up_to_message = "Введите цену до: "

sell_payment_label = "Разместить объявление!"
sell_payment_title = "Оплата"
sell_payment_description = "Оплата за размещение объявления"
successful_payment_message = "Оплата произведена успешно!"

show_project_message = (
    "<b>Название:</b> {name}\n<b>Тематика:</b> {theme}\n<b>Подписчиков:</b> {subs}\n<b>Доход в "
    "месяц:</b> {income}\n\n<b>Комментарий:</b> {comm}\n\n<b>Продавец:</b> @{"
    "seller}\n\n<b>Цена:</b> {price}\n\nГарантируем 100% безопасность при сделках в "
    "Telegram.\n<b>Гарант:</b> {guarantee} "
)

MESSAGES = {
    "start": start_message,
    "sell_menu": sell_menu_message,
    "put_up_for_sale": put_up_for_sale_massage,
    "project_name": project_name_question,
    "price": price_question,
    "price_check": price_check_question,
    "subscribers": subscribers_question,
    "subscribers_check": subscribers_check_question,
    "themes": themes_question,
    "themes_warn": themes_warn_question,
    "themes_warn_2": themes_warn_2_question,
    "themes_plus_1": themes_plus_1_question,
    "themes_plus": themes_plus_question,
    "yes": yes_question,
    "no": no_question,
    "income": income_question,
    "income_check": income_check_question,
    "comment": comment_question,
    "confirm": confirm_question,
    "cancellation": cancellation_question,
    "save_project": save_project_question,
    "get_list_of_projects": get_list_of_projects_message,
    "main_menu": main_menu_massage,
    "buy_menu": buy_menu_message,
    "chose_themes": chose_themes_message,
    "chose_price_from": chose_price_from_message,
    "chose_price_up_to": chose_price_up_to_message,
    "sell_payment": sell_payment_label,
    "sell_payment_title": sell_payment_title,
    "sell_payment_description": sell_payment_description,
    "successful_payment": successful_payment_message,
    "show_project": show_project_message,
}
