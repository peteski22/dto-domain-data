import uuid
from http import HTTPStatus

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, HTTPException
from pydantic import ValidationError

from container import AppContainer
from dtos.jobs import Job
from services.jobs_service import JobsService

router = APIRouter(prefix="/jobs")


@router.get("/", tags=["Jobs"])
@inject
async def get_jobs(
    jobs_service: JobsService = Depends(Provide[AppContainer.services.jobs_service]),
) -> list[Job]:
    try:
        return [Job.model_validate(job) for job in jobs_service.get_jobs()]
    except ValidationError as err:
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            detail=f"internal server error getting jobs: {err}",
        )


@router.get("/{job_id}", tags=["Jobs"])
@inject
async def get_job(
    job_id: uuid.UUID,
    jobs_service: JobsService = Depends(Provide[AppContainer.services.jobs_service]),
) -> Job:
    job = jobs_service.get_job(job_id)

    if job is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND.value,
            detail=f"job {job_id} does not exist",
        )

    try:
        Job.model_validate(job)
    except ValidationError:
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR.value,
            detail="internal server error validating stored job",
        )

    return job


# @app.post("/jobs")
# async def create_job(request: JobDto):
#     request.data
#     response = jobs_service.create_job()
#
