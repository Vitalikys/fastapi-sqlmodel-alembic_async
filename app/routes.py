from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, delete, update
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.db_async import get_session
from app.models import Song, SongBase

router = APIRouter()


@router.get("/songs", response_model=list[Song])
async def get_all_songs(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Song))
    songs = result.scalars().all()
    return [Song(name=song.name, artist=song.artist, id=song.id) for song in songs]


@router.post("/songs")
async def add_song(song: SongBase, session: AsyncSession = Depends(get_session)):
    song = Song(name=song.name, artist=song.artist, year=song.year)
    session.add(song)
    await session.commit()
    await session.refresh(song)
    return song


@router.get('/song/{song_id}')
async def get_one_song(song_id: int, session: AsyncSession = Depends(get_session)):
    """ https://ahmed-nafies.medium.com/sqlalchemy-async-orm-is-finally-here-d560dfaa335d """
    query = select(Song).where(Song.id == song_id)
    result = await session.execute(query)
    song = result.one_or_none()
    if not song:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='No such song !')
    print('song to find: ', song)
    return song


@router.delete("/song/{song_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_song(song_id: int, session: AsyncSession = Depends(get_session)):
    query = delete(Song).where(Song.id == song_id)
    await session.execute(query)
    await session.commit()
    # await session.delete(result)
    return {'message': "delete success"}


@router.put("/song/{song_id}", status_code=status.HTTP_200_OK)
async def update_song(song_id: int,
                      song: SongBase,
                      session: AsyncSession = Depends(get_session)
                      ):
    print('song_ dict: ', *song)
    query = update(Song).where(Song.id == song_id).values(
        name=song.name,
        artist=song.artist,
        year=song.year
    )
    await session.execute(query)
    await session.commit()
    return {'updated': 'ok'}


