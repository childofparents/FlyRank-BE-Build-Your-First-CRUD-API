from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Stage 2 Example tasks
tasks = [
    {"id": 1, "title": "Buy boba tea", "done": False},
    {"id": 2, "title": "Go grocery shopping", "done": False},
    {"id": 3, "title": "Clean the house", "done": True},
]

# Stage 3
class TaskCreate(BaseModel):
    title: Optional[str] = None

# Stage 4
class TaskUpdate(BaseModel):
    title: Optional[str] = None
    done: Optional[bool] = None

# Stage 1
@app.get("/")
async def root():
    return {"name": "Task API", "version": "1.0", "endpoint": ["/tasks"]}

#Stage 1
@app.get("/health")
async def health():
    return {"status": "ok"}

# Stage 2 Read (GET) - List of tasks
@app.get("/tasks")
async def get_tasks():
    return tasks

# Stage 2 Read (GET) - A specific task
@app.get("/tasks/{task_id}")
async def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return JSONResponse(status_code=404, content={"error": f"Task {task_id} not found"})

# Stage 3 Create (POST)
@app.post("/tasks", status_code=201)
async def create_task(task: TaskCreate):
    if not task.title or not task.title.strip():
        return JSONResponse(status_code=400, content={"error": "title is required"})

    next_id = max((t["id"] for t in tasks), default=0) + 1
    new_task = {"id": next_id, "title": task.title, "done": False}
    tasks.append(new_task)
    return new_task

# Stage 4 Update (PUT)
@app.put("/tasks/{task_id}")
async def update_task(task_id: int, update: TaskUpdate):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if task is None:
        return JSONResponse(status_code=404, content={"error": f"Task {task_id} not found"})

    if update.title is None and update.done is None:
        return JSONResponse(status_code=400, content={"error": "provide title and/or done to update"})

    if update.title is not None and not update.title.strip():
        return JSONResponse(status_code=400, content={"error": "title cannot be empty"})

    if update.title is not None:
        task["title"] = update.title
    if update.done is not None:
        task["done"] = update.done

    return task

# Stage 4 Delete (DELETE) a task
@app.delete("/tasks/{task_id}", status_code=204)
async def delete_task(task_id: int):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if task is None:
        return JSONResponse(status_code=404, content={"error": f"Task {task_id} not found"})

    tasks.remove(task)
    return Response(status_code=204)