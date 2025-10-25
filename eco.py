import telebot
import random

# --- Твой токен (замени на свой) ---
TOKEN = ""

bot = telebot.TeleBot(TOKEN)

# --- Список советов ---
eco_tips = [
    "🌊 Используй многоразовую бутылку вместо пластиковой 💧",
    "💡 Выключай свет, когда выходишь из комнаты 🔌", 
    "🔋 Сдавай батарейки и лампочки в специальные контейнеры ♻️",
    "🗑️ Сортируй мусор: пластик, стекло, бумама 📊",
    "🛍️ Бери с собой тканевую сумку в магазин 🌿",
    "🚲 Чаще ходи пешком или используй велосипед вместо машины 🌱",
    "💧 Экономь воду - выключай кран, когда чистишь зубы 🚰",
    "📱 Не меняй гаджеты без необходимости - уменьшай электронные отходы 📱"
]



@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "🌿 Привет! Я твой ЭкоБот! 🌍\n"
        "Я помогу тебе заботиться о нашей планете! 🌎\n\n"
        "📝 Напиши /sovet чтобы получить экологичный совет\n"
        "📋 Напиши /problems чтобы узнать о проблемах экологии\n"
        "❓ Напиши /help для списка команд"
    )


@bot.message_handler(commands=['sovet'])
def sovet(message):
    tip = random.choice(eco_tips)
    bot.send_message(message.chat.id, "💡 Экосовет:\n\n" + tip + "\n\n✨ Каждый маленький шаг важен! 🌟")

@bot.message_handler(commands=['problems'])
def send_problems(message):
    problems_text = """🌍 🔥 Проблемы загрязнения окружающей среды:

1️⃣ 🌫️ Загрязнение воздуха
https://ru.ruwiki.ru/wiki/%D0%97%D0%B0%D0%B3%D1%80%D1%8F%D0%B7%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5_%D0%B0%D1%82%D0%BC%D0%BE%D1%81%D1%84%D0%B5%D1%80%D1%8B_%D0%97%D0%B5%D0%BC%D0%BB%D0%B8

2️⃣ 💧 Загрязнение вод  
https://ru.ruwiki.ru/wiki/%D0%97%D0%B0%D0%B3%D1%80%D1%8F%D0%B7%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5_%D0%B2%D0%BE%D0%B4%D0%BD%D0%BE%D0%B9_%D1%81%D1%80%D0%B5%D0%B4%D1%8B

3️⃣ 🌱 Загрязнение почв
https://journal.sovcombank.ru/esg/zagryaznenie-pochvi-prichini-i-posledstviya

4️⃣ 🗑️ Накопление твёрдых отходов
https://vyvoz-musora24.ru/article/ekologicheskaya-problema-musora/

5️⃣ 🥤 Пластиковое загрязнение
https://ru.wikipedia.org/wiki/%D0%9F%D0%BB%D0%B0%D1%81%D1%82%D0%B8%D0%BA%D0%BE%D0%B2%D0%BE%D0%B5_%D0%B7%D0%B0%D0%B3%D1%80%D1%8F%D0%B7%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5

6️⃣ 🐾 Снижение биоразнообразия
https://ru.ruwiki.ru/wiki/%D0%A3%D1%82%D1%80%D0%B0%D1%82%D0%B0_%D0%B1%D0%B8%D0%BE%D1%80%D0%B0%D0%B7%D0%BD%D0%BE%D0%BE%D0%B1%D1%80%D0%B0%D0%B7%D0%B8%D1%8F

7️⃣ 🌧️ Кислотные осадки
https://yandex.ru/pogoda/ru/blog/kislotnye_dozhdi

8️⃣ 🕶️ Разрушение озонового слоя
https://en.wikipedia.org/wiki/Ozone_depletion

9️⃣ 🔊 Шумовое загрязнение
https://ru.wikipedia.org/wiki/%D0%A8%D1%83%D0%BC%D0%BE%D0%B2%D0%BE%D0%B5_%D0%B7%D0%B0%D0%B3%D1%80%D1%8F%D0%B7%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5

🔟 💡 Световое загрязнение
https://ru.ruwiki.ru/wiki/%D0%A1%D0%B2%D0%B5%D1%82%D0%BE%D0%B2%D0%BE%D0%B5_%D0%B7%D0%B0%D0%B3%D1%80%D1%8F%D0%B7%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5

💚 Вместе мы можем изменить мир к лучшему! 🌟"""
    
    bot.send_message(message.chat.id, problems_text)

@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = """🆘 📋 Доступные команды:

/start - 🏁 Начать работу с ботом
/problems - 📊 Показать основные проблемы загрязнения окружающей среды
/sovet - 💡 Получить случайный совет по защите окружающей среды
/help - ❓ Показать это сообщение

🌱 Давайте вместе заботиться о нашей планете! 🌍"""
    
    bot.send_message(message.chat.id, help_text)

@bot.message_handler(func=lambda m: True)
def echo(message):
    bot.send_message(message.chat.id, "🤔 Напиши /sovet чтобы получить совет 🌿\n"
                     "или /help для списка команд 📋")

print("🤖 Бот запущен... Нажми Ctrl+C для остановки. ⚡")
bot.polling(none_stop=True)
