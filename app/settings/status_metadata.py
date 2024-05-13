from pydantic import BaseModel


STATUS_MESSAGE: dict[int, str] = {
    100: "Game is on",
    101: "Game is on",
    201: "Game finished",
    202: "Game finished",
}


class StatusMetadata(BaseModel):
    """Metadata for game status

    Attributes:
        game_id: id of game for getting data
        status: status of game
        message: 'Game is on!' for status 1** and
                'Game is finished!' for status 2**
        additional: More detailed description of status
        words: all words used in game
    """

    game_id: int
    status: int
    message: str
    additional: str
    words: list[str]
