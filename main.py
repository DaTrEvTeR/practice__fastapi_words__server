import fastapi
from app.database import work_with_db


app = fastapi.FastAPI()


@app.on_event("startup")
async def startup() -> None:
    """
    Init tables in db on startup
    """
    work_with_db.init_tables()


@app.get("/")
async def index() -> None:
    """
    Choose started room or start new game
    """
    ...


@app.get("/start-game/")
async def start_game() -> None:
    """
    Create new room for game session
    """
    ...


@app.get("/{room_id}/")
async def check_room_status(room_id) -> None:
    """
    Check room status(notExist|continues|end)
    """
    ...


@app.post("/{room_id}/")
async def post_word(room_id) -> None:
    """
    Check new word
    and if it is ok send to server
    """
    ...
