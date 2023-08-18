import text

# В этом модуле находятся все принты и инпуты (взаимодействие с пользователем)

def main_menu() -> int:
    print(text.main_menu) # Вывод на экран главного меню
    while True:
        choice = input(text.input_choice)
        # Проверка на "дурака": при неправильном вводе, если ввод не число или большое число, возврат в пункт меню
        if choice.isdigit() and 0 < int(choice) < 100:
            return int(choice)

# функция, отвечающая за печать сообщений
def print_message(message: str):
    print('\n' + '='*len(message))  # подсчет длины сообщения и печать символов (=) в количестве, равным длине сообщения
    print(message)                   # печать сообщения
    print('=' * len(message) + '\n')  # печать символов (=) в количестве, равным длине сообщения

# функцияЮ отвечающая за печать сообщений
def print_note(book: list[dict[str,str]], error: str):
    if book:
        print('\n' + '='*71)
        for notes in book:
            print(f'{notes.get("id"):>3}. {notes.get("note"):<20} | {notes.get("data"):<20} | {notes.get("comment"):<20} ')  # форматирование вывода на печать

        print('=' * 71 + '\n')
    else:
        print_message(error)

# функция для ввода записи
def input_note(message) -> dict[str,str]:
    new = {}
    print(message)
    for key, txt in text.new_note.items():
        value = input(txt)
        if value:
            new[key] = value
    return  new


def input_search(message) -> str:
    return input(message)



