from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Stage 2
tasks = [
    {"id": 1, "title": "Buy boba tea", "done": False},
    {"id": 2, "title": "Go grocery shopping", "done": False},
    {"id": 3, "title": "Clean the house", "done": True},
]

# Stage 3
class TaskCreate(BaseModel):
    title: Optional[str] = None

# Stage 1
@app.get("/")
async def root():
    return {"name": "Task API", "version": "1.0", "endpoint": ["/tasks"]}

#Stage 1
@app.get("/health")
async def health():
    return {"status": "ok"}

# Stage 2
@app.get("/tasks")
async def get_tasks():
    return tasks

# Stage 2
@app.get("/tasks/{task_id}")
async def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return JSONResponse(status_code=404, content={"error": f"Task {task_id} not found"})

# Stage 3
@app.post("/tasks", status_code=201)
async def create_task(task: TaskCreate):
    if not task.title or not task.title.strip():
        return JSONResponse(status_code=400, content={"error": "title is required"})

    next_id = max((t["id"] for t in tasks), default=0) + 1
    new_task = {"id": next_id, "title": task.title, "done": False}
    tasks.append(new_task)
    return new_task