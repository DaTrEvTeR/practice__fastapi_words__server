from app.database.db_connection import DbConnection
# from db_connection import DbConnection


def init_tables() -> None:
    """
    Create tables in db if them not exists

    :return: None
    """
    with DbConnection() as connection:
        connection.execute("""
                CREATE TABLE IF NOT EXISTS words (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    gameid INTEGER,
                    word TEXT NOT NULL
                    )
            """)
        connection.execute("""CREATE TABLE IF NOT EXISTS games_status (
                    gameid INTEGER PRIMARY KEY,
                    status INTEGER
                )""")


def get_id_unfinished_rooms() -> list:
    """
    Get all id of unfinished games

    :return: list with all id of unfinished games
    """
    with DbConnection() as connection:
        res = connection.execute(
            "SELECT gameid FROM games_status WHERE status IN (?, ?)", (100, 101)
        ).fetchall()

    return [id[0] for id in res]


def create_new_room() -> int:
    """
    Create new note with new room id in games_status table

    :return: id of created room
    """
    new_room_id = get_last_game_id() + 1
    with DbConnection() as connection:
        connection.execute(
            """
                INSERT INTO games_status (gameid, status) VALUES (?, ?)
                """,
            (new_room_id, 100),
        )

    return new_room_id


def get_game_status(gameid) -> int:
    """
    If give a non-existent game ID, it will raise an error

    :param gameid: id of game which need get status
    :return: True if game not ended
    """
    with DbConnection() as connection:
        result = connection.execute(
            """
        SELECT status FROM games_status WHERE gameid=?""",
            (gameid,),
        ).fetchone()

        if result:
            return result[0]
        else:
            raise ValueError("Gameid not found")


def change_game_status(gameid, status) -> None:
    """
    Change status of game to 'ended'

    :param gameid: id of game which status need to change
    :return: None
    """
    with DbConnection() as connection:
        connection.execute(
            """
        UPDATE games_status SET status=(?) WHERE gameid=(?)""",
            (status, gameid),
        )


def add_word(word: str, gameid: int) -> None:
    """
    Add word to database

    :param word: word that needs to be added to the database
    :param gameid: id of game to add the word to
    :return: None
    """
    with DbConnection() as connection:
        connection.execute(
            """
        INSERT INTO words (word, gameid) VALUES (?, ?)
        """,
            (word, gameid),
        )


def get_last_game_id() -> int:
    """
    Get last game id from table games_status

    :return: id of last game or 0
    if there is no games yes
    """
    with DbConnection() as connection:
        result = connection.execute("SELECT MAX(gameid) FROM games_status").fetchone()

    return result[0] if result[0] else 0


def get_last_word(gameid: int) -> str:
    """
    Get last word of game from database

    :param gameid: gameid
    :return: last word of game
    """
    with DbConnection() as connection:
        res = connection.execute(
            "SELECT word FROM words WHERE gameid=?", (gameid,)
        ).fetchone()

    return res[0] if res else ""


def word_already_used(word: str, gameid: int) -> bool:
    """
    Check if word already used in game

    :param word: word to check
    :param gameid: game id
    :return: True if word used and False if not
    """
    with DbConnection() as connection:
        request = connection.execute(
            """
        SELECT id FROM words WHERE word=? AND gameid=?
        """,
            (word, gameid),
        ).fetchone()

    return True if request else False


def get_list_all_words_of_game(gameid: int) -> list:
    """
    Get all words of this game.

    :param gameid: game id
    :return: list of all words
    """
    with DbConnection() as connection:
        request = connection.execute(
            """
            SELECT word FROM words WHERE gameid=?
            """,
            (gameid,),
        ).fetchall()

    return [word[0] for word in request]
