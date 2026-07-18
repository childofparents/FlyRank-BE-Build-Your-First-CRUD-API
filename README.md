# FlyRank-BE-Build-Your-First-CRUD-API
# W2 Assignment Repo

## Task API

A small CRUD API for managing a to-do list, built with FastAPI. Data is stored in memory — no database yet (that's next week's lesson, so losing data on restart is expected, not a bug).

Built for the FlyRank Internship Backend Track, Week 2: Build your first CRUD API.

## What this is
The API supports the four CRUD operations on tasks: create, read, update, and delete. Every task has an `id`, a `title`, and a `done` flag. You can explore and test it interactively via Swagger UI, or hit it directly with `curl`.

## 7 stages, committed after every stage:

0. Hello, server
1. Front door
2. Read
3. Create
4. Update & Delete
5. See it
6. Publish
7. (Bonus) AI rematch

## How to run it

1. Clone the repo and move into it:
   ```bash
   git clone https://github.com/childofparents/task-api.git
   cd task-api
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Start the server:
   ```bash
   uvicorn main:app --reload
   ```

4. Open **http://localhost:8000/docs** to try it in Swagger UI, or send requests with `curl` against `http://localhost:8000`.

## Endpoints

| Method | Path          | Description                                  |
|--------|---------------|-----------------------------------------------|
| GET    | `/`           | API info                                       |
| GET    | `/health`     | Health check                                   |
| GET    | `/tasks`      | List all tasks                                 |
| GET    | `/tasks/{id}` | Get a single task by id (404 if not found)     |
| POST   | `/tasks`      | Create a new task (400 if title missing/empty) |
| PUT    | `/tasks/{id}` | Update a task's title and/or done status       |
| DELETE | `/tasks/{id}` | Delete a task (204 on success)                 |

## Example request

```bash
curl -i -X POST http://localhost:8000/tasks -H "Content-Type: application/json" -d '{"title":"Buy milk"}'
```

```
HTTP/1.1 201 Created
content-type: application/json

{"id":4,"title":"Buy milk","done":false}
```

## Swagger UI

![Swagger UI screenshot](https://github.com/childofparents/FlyRank-BE-Build-Your-First-CRUD-API/blob/c8bb349d16768bb15642defbcccba6d157f00558/Stage%205/README%20%3Adocs.png)

## Status codes

- `200` — successful read
- `201` — task created
- `204` — task deleted (empty body)
- `400` — invalid input (e.g. missing/empty title), with a JSON body like `{"error": "..."}`
- `404` — task not found, with a JSON body like `{"error": "Task 99 not found"}`

## Notes

- All data lives in memory — restarting the server resets it back to the 3 seed tasks.
- No database or file storage is used yet.
