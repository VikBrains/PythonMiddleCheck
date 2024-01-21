import datetime
from colorama import Style, Fore

from controller import Controller
from JSON import JSON
from note import Note
from view import View


def run():
    c = Controller(JSON("notes.json"), View())

    while True:
        command = input('\n'
                        '1 - Создать заметку\n'
                        '2 - Просмотреть заметку\n'
                        '3 - Изменить заметку\n'
                        '4 - Удалить заметку\n'
                        '5 - Просмотреть все заметки\n'
                        '6 - Выход\n' +
                        'Напишите число - Ваш выбор: '
                        )
        if command == '6':
            break

        if command == '1':
            print(Fore.GREEN + '\nСоздать заметку:' + Style.RESET_ALL)
            c.create_note(get_note_data())

        elif command == '2':
            print(Fore.GREEN + '\nПросмотреть заметку:' + Style.RESET_ALL)
            if c.notes_exist():
                c.show_note(int(get_number()))

        elif command == '3':
            if c.notes_exist():
                print(Fore.YELLOW + '\nИзменить заметку:' + Style.RESET_ALL)
                updated_id = int(get_number())
                if c.note_id_exist(updated_id):
                    c.update_note(updated_id, get_note_data())

        elif command == '4':
            if c.notes_exist():
                print('\nУдалить заметку:')
                if (input(Fore.RED + 'Вы точно хотите удалить эту заметку? '
                                    '(Y/N): ' + Style.RESET_ALL).capitalize() == 'Y'):
                    delete_id = int(get_number())
                    if c.note_id_exist(delete_id):
                        c.delete_note(delete_id)

        elif command == '5':
            if c.notes_exist():
                print(Fore.GREEN + '\nСписок всех заметок:' + Style.RESET_ALL)
                c.show_notes()
        else:
            print(Fore.RED + 'Команда не найдена' + Style.RESET_ALL)


def get_note_data():
    note_id = 0
    date = datetime.datetime.now()
    title = input('Введите заголовок заметки: ')
    text = input('Введите тело заметки: ')
    return Note(note_id, date, title, text)


def get_number():
    while True:
        get_choice = input('Введите id заметки: ')
        if get_choice.isdigit() and int(get_choice) > 0:
            return get_choice
        else:
            print(Fore.YELLOW + 'Введите целое положительное число!'
                  + Style.RESET_ALL)
