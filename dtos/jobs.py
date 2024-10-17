import uuid
from enum import Enum

from pydantic import BaseModel, ConfigDict


class Status(str, Enum):
    Pending = "Pending"
    Failed = "Failed"
    Completed = "Completed"


class Job(BaseModel):
    model_config = ConfigDict(
        frozen=True,
        from_attributes=True,
    )

    id: uuid.UUID = uuid.uuid4()
    name: str
    status: Status = Status.Pending
