import telebot
import random

token = ""

bot = telebot.TeleBot(token)

HELP = """
/help или /start - помощь с ботом.
/add или /todo - добавить задачу в список (пример: /add сегодня Изучить Python).
/show или /print - показать все добавленные задачи за время (пример: /show сегодня).
/random - добавлять случайную задачу на сегодня.
/count - сколько сообщений отправлено в чат?.
/bye - он попрощается."""

RANDOM_TASKS = ["Записаться на курс в Нетологию", "Написать Гвидо письмо", "Покормить кошку", "Помыть машину"]

tasks = {}

def add_todo(date, task):
  if date in tasks:
      tasks[date].append(task)
  else:
      tasks[date] = []
      tasks[date].append(task)

@bot.message_handler(commands=["help", "start"])
def help(message):
    bot.send_message(message.chat.id, HELP)

@bot.message_handler(commands=["bye"])
def exit(message):
    txt = "Бот остановлен. Спасибо за использование!)"
    bot.send_message(message.chat.id, txt)
    
@bot.message_handler(commands=['count'])
def chatting(message):
    bot.send_message(message.chat.id, message.id)

@bot.message_handler(commands=["add", "todo"])
def add(message):
    command = message.text.split(maxsplit=2)
    date = command[1].lower()
    task = command[2]
    add_todo(date, task)
    text = "Задача " + task + " добавлена на дату " + date
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["random"])
def random_add(message):
    date = "сегодня"
    task = random.choice(RANDOM_TASKS)
    add_todo(date, task)
    text = "Задача " + task + " добавлена на дату " + date
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["show", "print"])
def show(message):
    command = message.text.split(maxsplit=1)
    date = command[1]
    text = ""
    if date in tasks:
        text = date.upper() + "\n"
        for task in tasks[date]:
            text = text + " · " + task + "\n"
    else:
        text = "Задачи на эту дату нет"
    bot.send_message(message.chat.id, text)

bot.polling(none_stop=True)
