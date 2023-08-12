main_menu = '''\nГлавное меню:
     1. Открыть заметку
     2. Сохранить заметку
     3. Показать все заметки
     4. Добавить заметку
     5. Найти запись
     6. Изменить заметку
     7. Удалить заметку
     8. Выход\n'''

input_choice = 'выберите пункт меню: '

load_successful = 'Заметки успешно открылись'

save_successful = 'Заметка успешно сохранена'

nb_empty = 'Список заметок пуст или не загружен'

input_new_note = 'Введите новую заметку: '

new_note = {
            'note': 'Введите инфо: ',
            'data': 'Введите дату: ',
            'comment': 'Введите комментарий: '}

def new_note_successful(note: str):
    return f'Новая заметка успешно добавлена'

input_search = 'Что будем искать?'

def empty_search(word) -> str:
    return f'Записи, содержащие "{word}" не найдены(('

input_change = 'Какую заметку будем менять?'
input_index = 'Введите индекс контакта:  '

change_note = 'Ведите изменения: '

def change_successful(note: str) -> str:
    return  f'Запись {note} успешно изменена'