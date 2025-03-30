from typing import Annotated

from fastapi import APIRouter, status, Depends

from dependecy import get_task_service, get_tasks_repository
from repository import TaskRepository
from schema.task import TaskSchema
from service import TaskService

router = APIRouter(prefix="/task", tags=["task"])


@router.get(
    "/all",
    response_model=list[TaskSchema]
)
async def get_tasks(
        task_service: Annotated[TaskService, Depends(get_task_service)]
):
    return task_service.get_tasks()


@router.post(
    "/",
    response_model=TaskSchema
)
async def create_tasks(
        task: TaskSchema,
        task_repository: Annotated[TaskRepository, Depends(get_tasks_repository)]
):
    task.id = task_repository.create_task(task)
    return task


@router.patch(
    "/{task_id}",
    response_model=TaskSchema
)
async def patch_tasks(
        task_id: int,
        name: str,
        task_repository: Annotated[TaskRepository, Depends(get_tasks_repository)]
):
    return task_repository.update_name(task_id, name)


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tasks(
        task_id: int,
        task_repository: Annotated[TaskRepository, Depends(get_tasks_repository)]
):
    task_repository.delete_task(task_id)
    return {"message": "Task deleted successfully"}
