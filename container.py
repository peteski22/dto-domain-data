from dependency_injector import containers, providers

from services.jobs_service import JobsService


class ServicesContainer(containers.DeclarativeContainer):
    jobs_service = providers.Factory(JobsService)


class AppContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        # Where to inject our dependencies...
        modules=["api.routes"]
    )

    services = providers.Container(ServicesContainer)
