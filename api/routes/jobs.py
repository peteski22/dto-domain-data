import uuid
from http import HTTPStatus

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, HTTPException
from pydantic import ValidationError

from container import AppContainer
from dtos.jobs import Job
from services.jobs_service import JobsService


router = APIRouter()


@router.get("/")
@inject
async def get_jobs(
    jobs_service: JobsService = Depends(Provide[AppContainer.jobs_service]),
) -> list[Job]:
    try:
        return [Job.model_validate(job) for job in jobs_service.get_jobs()]
    except ValidationError as err:
        raise HTTPException(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            detail=f"internal server error getting jobs: {err}",
        )


@router.get("/{job_id}")
@inject
async def get_job(
    job_id: uuid.UUID,
    jobs_service: JobsService = Depends(Provide[AppContainer.jobs_service]),
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


@router.post("/", status_code=HTTPStatus.CREATED)
@inject
async def create_job(
    name: str, jobs_service: JobsService = Depends(Provide[AppContainer.jobs_service])
) -> Job:
    name = name.strip()
    if name == "":
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST.value,
            detail="name cannot be empty",
        )

    job = jobs_service.create_job(name)
    Job.model_validate(job)
    return job


@router.put(
    "/{job_id}",
    responses={
        HTTPStatus.OK.value: {"model": Job},
        HTTPStatus.CREATED.value: {"model": Job},
    },
)
@inject
async def update_job(
    job_id: uuid.UUID,
    job: Job,
    jobs_service: JobsService = Depends(Provide[AppContainer.jobs_service]),
) -> Job:
    name = job.name.strip()
    if name == "":
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST.value,
            detail="name cannot be empty",
        )

    # TODO: If the resource doesn't exist we need to create it and return 201.
    job = jobs_service.update_job(job)
    if job is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND.value,
            detail=f"job {job_id} does not exist",
        )

    Job.model_validate(job)
    return job
