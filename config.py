import os

# Bot Data
TOKEN = os.getenv("TELEGRAM_TOKEN") # Get your bot token using https://t.me/BotFather

# Support Chat
CHAT_ID = os.getenv("CHAT_ID") # To find out your channels ID use: https://t.me/getidsbot

# Database Data
DATABASE_URL = os.getenv("DATABASE_URL")
REMOVAL_INTERVAL = os.getenv("ROW_REMOVAL_INTERVAL")

# Predefined text to send
TEXT_MESSAGES = {
    'start': 'Ласкаво просимо 👋\n\nНапишіть своє запитання / пропозицію, і ми відповімо Вам найближчим часом.',
    'message_template': '<i>Повідомлення від: <b>@{0}</b>.</i>\n\n{1}<b>id: {2}</b>\n<b>msg_id: {3}</b>',
    'is_banned': '❌ Користувач забанений!', 'has_banned': '✅ Користувач був успішно забанений!',
    'already_banned': '❌ Користувач уже забанений!', 'has_unbanned': '✅ Користувач був успішно розбанений!',
    'not_banned': '❌ Такого користувача немає в бан-лісті!',
    'user_banned': '🚫 Ви більше не можете писати в бот пропозицій!',
    'user_reason_banned': '🚫 Ви більше не можете писати в бот пропозицій через причину: <i>{}</i>.',
    'user_unbanned': '🥳 Сама благодать зійшла з небес, і тепер ви знову можете писати до боту пропозицій!',
    'pending': 'Дякуємо за ваше звернення. Ми вже оброблюємо Ваш запит!',
    'unsupported_format': '❌ Формат вашого повідомлення не підтримується, воно не буде переслане.',
    'message_not_found': '❌ Схоже, що ви відправляли повідомлення більше трьох діб тому, повідомлення не було знайдено!'
    , 'message_was_not_edited': '❌ На жаль не можна редагувати зображення в повідомленнях. '
                                'Будь ласка, надішліть нове зображення',
    'reply_error': '❌ Будь-ласка, давайте відповідь /ban або /unban лише на переслані від користувачів повідомлення!'
}
