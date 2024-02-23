from typing import Optional

from pydantic import BaseModel


class STaskAdd(BaseModel):
    name: str
    description: Optional[str] = None

class STask(BaseModel):
     id: int

class STaskID(BaseModel):
    ok: bool=True
    task_id: int