import random

HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи.
random - добавлять случайную задачу на дату Сегодня.
count - подсчет задач на дату.
exit - выход из программы."""

RANDOM_TASKS = ["Записаться на курс в Нетологию", "Написать Гвидо письмо", "Покормить кошку", "Помыть машину"]

tasks = {

}

run = True

def add_todo(date, task):
  if date in tasks:
      tasks[date].append(task)
  else:
      tasks[date] = []
      tasks[date].append(task)
  print("Задача ", task, " добавлена на дату ", date)

def count_letter(date, letter):
  k = 0
  for word in tasks[date]:
    if letter in word:
      k = k + 1
  print(k)
  return k

while run:
  command = input("Введите команду: ")
  if command == "help":
    print(HELP)
  elif command == "show":
    date = input("Введите дату для отображения списка задач: ")
    if date in tasks:
      for task in tasks[date]:
        print('- ', task)
    else:
      print("Такой даты нет")
  elif command == "add":
    date = input("Введите дату для добавления задачи: ")
    task = input("Введите название задачи: ")
    add_todo(date, task)
  elif command == "random":
    task = random.choice(RANDOM_TASKS)
    add_todo("Сегодня", task)
  elif command == "count":
    date = input("Введите дату для подсчета задач: ")
    letter = input("Введите букву: ")
    count_letter(date,letter)
  elif command == "exit":
    print("Спасибо за использование бота!")
    break
  else:
    print("Неизвестная команда")

print("До свидания!")