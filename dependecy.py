from fastapi import Depends

from repository import TaskRepository, TaskCache
from cache import get_redis_connection
from database import get_db_session
from service import TaskService


def get_tasks_repository() -> TaskRepository:
    db_session = get_db_session()
    return TaskRepository(db_session)


def get_tasks_cache_repository() -> TaskCache:
    redis_connection = get_redis_connection()
    return TaskCache(redis_connection)


def get_task_service(
    tasks_repository: TaskRepository = Depends(get_tasks_repository),
    tasks_cache: TaskCache = Depends(get_tasks_cache_repository)
) -> TaskService:
    return TaskService(
        task_repository=tasks_repository,
        task_cache=tasks_cache
    )