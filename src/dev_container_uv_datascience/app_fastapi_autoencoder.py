import uvicorn
from fastapi import FastAPI, Response

app = FastAPI()


# ROOT endpoint
@app.get("/")
def read_root() -> Response:
    """Root endpoint that provides information about the API."""

    message = """
    ⚡⚡⚡ Welcome to the FastAPI API! ⚡⚡⚡
    """
    return Response(content=message, media_type="text/plain")


# Application entry point
if __name__ == "__main__":
    # Run the FastAPI application
    uvicorn.run(app, host="0.0.0.0", port=8000)
