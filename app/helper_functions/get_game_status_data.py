from app.settings.status_metadata import StatusMetadata
from app.database.work_with_db import (
    get_game_status,
    get_list_all_words_of_game,
    get_last_word,
)


STATUS_MESSAGE: dict[int, str] = {
    100: "Game is on",
    101: "Game is on",
    201: "Game finished",
    202: "Game finished",
}


def get_additional_message(gameid, gamestatus):
    """
    Get additional status info
    """
    match gamestatus:
        case 100:
            return "Enter first word"
        case 101:
            last_word = get_last_word(gameid)
            return f"Last word {last_word}, nex word starts with {last_word[-1]}"
        case 201:
            return "Incorrect first letter"
        case 202:
            return "Word already used in game"


def get_game_status_data(gameid) -> dict:
    """
    Get all data about game data
    """
    try:
        game_status = get_game_status(gameid)
        return StatusMetadata(
            game_id=int(gameid),
            status=game_status,
            message=STATUS_MESSAGE[game_status],
            additional=get_additional_message(gameid, game_status),
            words=get_list_all_words_of_game(gameid),
        )
    except ValueError:
        return {"message": "Room not found"}
