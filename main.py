from container import AppContainer
from api.router import Router


# Wire up dependency injection.
container = AppContainer()

# Spin up the API server.
app = Router.create_app()
