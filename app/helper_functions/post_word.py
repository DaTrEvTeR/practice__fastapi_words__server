from app.database.work_with_db import get_game_status, change_game_status, add_word
from app.helper_functions.check_word import check_word


def post_word_in_server(room_id, word):
    try:
        if get_game_status(room_id) in (100, 101):
            res = check_word(word, int(room_id))
            change_game_status(room_id, res)
            if res == 101:
                add_word(word, room_id)
                return "Word add"
            return "Game ended"

        else:
            return "You can`t add word to finished game"
    except ValueError:
        return "Room not found"
