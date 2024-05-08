from app.database.work_with_db import word_already_used, get_last_word


def check_word(word: str, gameid: int):
    """
    Make all checks before add word to db, if word incorrect finish game
    """
    if get_last_word(gameid)[-1] != word[0]:
        return 201
    elif word_already_used(word, gameid):
        return 202
    else:
        return 101
