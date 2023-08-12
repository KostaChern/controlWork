from typing import Dict

import text
import view
import model


def start():
    while True:
        choice = view.main_menu()

        match choice:
            case 1:
                model.open_nb()
                view.print_message(text.load_successful)
            case 2:
                model.save_nb()
                view.print_message(text.save_successful)
            case 3:
                nb = model.get_nb()
                view.print_note(nb, text.nb_empty)
            case 4:
                note: dict[str, str] = view.input_note(text.input_new_note)
                model.add_note(note)
                view.print_message(text.new_note_successful(note))
            case 5:
                key_word = view.input_search(text.empty_search())
                result = model.search_note(key_word)
                view.print_note(result, text.empty_search(key_word))
            case 6:
                key_word = view.input_search(text.input_change)
                result = model.search_note(key_word)
                if result:
                    if len(result) != 1:
                        view.print_note(result, '')
                        current_id = view.input_search(text.input_index)
                    else:
                        current_id = result[0].get('id')
                    new_note = view.input_note(text.change_note)
                    note = model.change_note(new_note, current_id)
                    view.print_message(text.change_successful(note))
                else:
                    view.print_message(text.empty_search(key_word))


            case 7:
                pass
            case 8:
                break


