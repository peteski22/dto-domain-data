from dependency_injector import containers, providers

from services.jobs_service import JobsService
from repository.jobs_repository import JobsRepository


class AppContainer(containers.DeclarativeContainer):
    providers.Configuration()
    jobs_repository = providers.Singleton(JobsRepository)
    jobs_service = providers.Singleton(JobsService, repository=jobs_repository)
    wiring_config = containers.WiringConfiguration(
        # Where to inject our dependencies...
        modules=[
            "api.routes.jobs",
            "services.jobs_service",
        ]
    )
