import uvicorn

from uv_datascience_project_template.app_fastapi_autoencoder import app
from uv_datascience_project_template.config import get_settings

# Application entry point
if __name__ == "__main__":
    settings = get_settings()
    # Run the FastAPI application
    # uvicorn.run(app=app, host="0.0.0.0", port=8000)
    uvicorn.run(app=app, host=settings.api.host, port=settings.api.port)
