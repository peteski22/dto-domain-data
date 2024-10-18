import uuid
from typing import Optional

from domain.jobs import Job, Status
from repositories.jobs_repository import JobsRepository


class JobsService:
    def __init__(self, repository: JobsRepository):
        self.repository = repository

    def get_jobs(self) -> [Job]:
        jobs = self.repository.get_jobs()
        return jobs

    def get_job(self, job_id: uuid.UUID) -> Optional[Job]:
        job = self.repository.get_job(job_id)

        return job

    def create_job(self, name: str) -> Job:
        job = Job(id=uuid.uuid4(), name=name, status=Status.Pending)
        self.repository.create_job(job)
        return job

    def update_job(self, job: Job) -> Optional[Job]:
        data = self.repository.get_job(job.id)
        if data is None:
            return None

        return self.repository.update_job(job)
