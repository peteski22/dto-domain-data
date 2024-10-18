import uuid
from typing import Optional

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from domain.jobs import Job as JobDomain, Status as StatusDomain
from data.jobs import Base, Job as JobData


class JobsRepository:
    def __init__(self):
        # self.engine = create_engine("sqlite:///local.db", echo=True)
        self.engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)
        Base.metadata.create_all(self.engine)

    @staticmethod
    def to_data(job: JobDomain) -> JobData:
        return JobData(
            id=job.id,
            name=job.name,
            status=job.status.value,
        )

    @staticmethod
    def to_domain(job: JobData) -> Optional[JobDomain]:
        if job is None:
            return None

        return JobDomain(id=job.id, name=job.name, status=StatusDomain(job.status))

    def get_jobs(self) -> list[JobDomain]:
        with Session(self.engine) as session:
            jobs = session.query(JobData).all()
            return [JobsRepository.to_domain(job) for job in jobs]

    def get_job(self, id: uuid.UUID) -> Optional[JobDomain] | None:
        with Session(self.engine) as session:
            job = session.query(JobData).where(JobData.id == id).first()
            return JobsRepository.to_domain(job)

    def create_job(self, job: JobDomain):
        data = JobsRepository.to_data(job)
        with Session(self.engine) as session:
            session.add(data)
            session.commit()

    def update_job(self, job: JobDomain) -> Optional[JobDomain]:
        data = JobsRepository.to_data(job)
        with Session(self.engine) as session:
            res = session.query(JobData).where(JobData.id == data.id).first()
            if res is None:
                return None

            res.id = data.id
            res.name = data.name
            res.status = data.status

            session.commit()
            session.refresh(res)
            return job
