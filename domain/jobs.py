from dataclasses import dataclass
from enum import Enum
import uuid


@dataclass()
class Status(str, Enum):
    Pending = "Pending"
    Failed = "Failed"
    Completed = "Completed"


@dataclass()
class Job:
    def __init__(self, id: uuid.UUID, name: str, status: Status):
        self.id = id
        self.name = name
        self.status = status
