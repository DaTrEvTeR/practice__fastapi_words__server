import fastapi
from fastapi.responses import JSONResponse
from app.database import work_with_db
from app.helper_functions.get_game_status_data import get_game_status_data
from app.helper_functions.post_word import post_word_in_server


app = fastapi.FastAPI()


@app.on_event("startup")
async def startup() -> None:
    """
    Init tables in db on startup
    """
    work_with_db.init_tables()


@app.get("/")
async def index() -> JSONResponse:
    """
    Choose started room or start new game
    """
    return {
        "message": 'Welcome to the "Words Game", choose one of existing room or create new',
        "unfinished_games": work_with_db.get_id_unfinished_rooms(),
    }


@app.get("/start-game/")
async def start_game() -> JSONResponse:
    """
    Create new room for game session
    """
    new_room_id = work_with_db.create_new_room()
    return {"message": "Created new room", "new_room_id": new_room_id}


@app.get("/{room_id}/")
async def check_room_status(room_id) -> JSONResponse:
    """
    Check room status(notExist|continues|end)
    """
    return get_game_status_data(room_id)


@app.post("/{room_id}/")
async def post_word(room_id, word) -> JSONResponse:
    """
    Check new word
    and if it is ok send to server
    """
    post_word_in_server(room_id, word)
