import uvicorn

from dev_container_uv_datascience.app_fastapi_autoencoder import app

# Application entry point
if __name__ == "__main__":
    # Run the FastAPI application
    uvicorn.run(app=app, host="0.0.0.0", port=8000)
