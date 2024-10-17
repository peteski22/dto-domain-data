import uuid

from domain.jobs import Job, Status


class JobsService:
    """Would usually be the service that deals with the presentation layer and the repository layer.

    e.g. Saving jobs to the DB, getting jobs from the DB.

    Here is where we would deal with the 'domain' objects.
    'controllers' would map domain objects to DTOs (and vice versa)
    'repositories' would map domain objects to Data (entity) types and vice versa.
    """

    def get_jobs(self) -> [Job]:
        jobs = [
            Job(
                name="job1",
                id="7e8afeac-1c49-4ba9-a0b9-c13f08a7b454",
                status=Status.Failed,
            ),
            Job(
                name="job2",
                id="6f4d1d75-d863-4ea4-9419-6c3a2aa86b4f",
                status=Status.Pending,
            ),
            Job(
                name="job3",
                id="2c886f69-21bc-4edf-88a6-1e599dd7f2c6",
                status=Status.Completed,
            ),
        ]
        return jobs

    def get_job(self, job_id: uuid.UUID) -> Job | None:
        for job in self.get_jobs():
            if job.id == job_id:
                return job

        return None
