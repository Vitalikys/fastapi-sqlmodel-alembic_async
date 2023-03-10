https://habr.com/ru/post/580866/

https://github.com/testdrivenio/fastapi-sqlmodel-alembic


# FastAPI + SQLModel + Alembic

Sample FastAPI project that uses async SQLAlchemy, SQLModel, Postgres, Alembic, and Docker.

## Want to learn how to build this?

Check out the [post](https://testdriven.io/blog/fastapi-sqlmodel/).

## Want to use this project?

```sh
$ docker compose up -d --build
$ docker compose exec web alembic upgrade head
```

Sanity check: [http://localhost:8004/ping](http://localhost:8004/ping)

Add a song:

```sh
$ curl -d '{"name":"Midnight Fit", "artist":"Mogwai", "year":"2021"}' -H "Content-Type: application/json" -X POST http://localhost:8004/songs
```

Get all songs: [http://localhost:8004/songs](http://localhost:8004/songs)

инициализируйте Alembic с помощью асинхронного шаблона:
```shell
$ docker compose exec web alembic init -t async migrations
```

Створити новий файл миграції:
```bash
$ docker compose exec web alembic revision --autogenerate -m "add year"
```

Примiнитu мiграцию:
```shell
$ docker compose exec web alembic upgrade head
```
Откройте логи контейнеров через docker-compose logs web.
```shell
$ docker compose logs web
```