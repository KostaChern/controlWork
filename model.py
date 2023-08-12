note_book: list[dict[str, str]] = []
path = 'note_book.txt'

def open_nb():
    global note_book
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for note in data:
        note = note.strip().split(':')
        new = {'id':note[0], 'note':note[1], 'data': note[2], 'comment': note[3]}
        note_book.append(new)

def save_nb():
    global note_book
    data = []
    for note in note_book:
        data.append(':'.join([value for value in note.values() ]))
    data = '\n'.join(data)
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(data)



def get_nb():
    global note_book
    return note_book

def add_note(new: dict[str, str]) -> str:
    global note_book
    new_id = int(note_book[-1].get('id')) + 1
    new["id"] = str(new_id)
    note_book.append(new)
    return new.get('note')

def search_note(word: str) -> list[dict[str, str]]:
    global note_book
    result: list[dict[str, str]] = []
    for note in note_book:
        for field in note.values():
            if word.lower() in field.lower():
                result.append(note)
                break
    return result

def change_note(new: dict, index: int):
    global note_book
    for entry in note_book:
        if index == entry.get('id'):

            entry['note'] = new.get('note', entry.get('note'))
            entry['data'] = new.get('data', entry.get('data'))
            entry['comment'] = new.get('comment', entry.get('comment'))
            return entry.get('note')




