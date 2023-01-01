from fastapi import FastAPI
from app.routes import router

app = FastAPI()
app.include_router(router)


# @app.on_event("startup")
# async def on_startup():
#     """ створення таблиць.
#     якщо є алембік то ми це видаляємо """
#     await init_db()

@app.get("/ping")
async def pong():
    return {"ping": "pong!"}


""" SYNC: 
@app.get("/songs", response_model=list[Song])
def get_songs(session: Session = Depends(get_session)):
    result = session.execute(select(Song))
    songs = result.scalars().all()
    return [Song(name=song.name, artist=song.artist, id=song.id) for song in songs]
@app.post("/songs")
def add_song(song: SongCreate, session: Session = Depends(get_session)):
    song = Song(name=song.name, artist=song.artist)
    session.add(song)
    session.commit()
    session.refresh(song)
    return song"""
