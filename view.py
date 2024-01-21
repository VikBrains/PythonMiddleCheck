
class View(object):

    @staticmethod
    def display_note_stored():                       # Создание заметки (п.1)
        print('\n---------- create report ----------\n')
        print('Заметка успешно добавлена!')
        print('--------------- end ---------------')

    @staticmethod
    def show_note(note):                              # Чтение заметки (п.2)
        print('\n+++ read note ++++++ read note +++')
        print(note)
        print('-------------- end --------------')

    @staticmethod
    def display_note_updated(note_id):               # Изменение заметки (п.3)
        print('\n-------- change note content --------\n')
        print('Заметка с id:{} успешно обновлена!'.format(note_id))
        # TODO show note
        print('----------------- end -----------------')

    @staticmethod
    def display_note_deletion(note_id):               # Удаление заметки (п.4)
        print('\n----------- deleting report -----------\n')
        print('Заметка с id: {} УДАЛЕНА!'.format(note_id))
        print('----------------- end -----------------')

    @staticmethod
    def show_number_point_list(notes):         # Выведение списка заметок (п.5)
        for note in notes:
            print('\n------------ next note ------------\n')
            print(note)
            print('--------------- end ---------------')

    @staticmethod
    def show_empty_list_message():                       # сообщение к (п.5)
        print('\n---------- absence message ----------\n')
        print('Список заметок пустой!')
        print('--------------- end ---------------')

    @staticmethod
    def display_note_id_not_exist(note_id):
        print('\n---------- absence message ----------\n')
        print('Заметка с id: {} не найдена!'.format(note_id))
        print('--------------- end ---------------')

    @staticmethod
    def display_note_id_exist(note_id):
        print('\n---------- excess message ----------\n')
        print('Заметка с id: {} уже есть!'.format(note_id))
        print('--------------- end ---------------')


def display_note_id_not_exist(search_id):
    return search_id
