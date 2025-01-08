# FastAPI LitAutoEncoder App Instructions

- [FastAPI LitAutoEncoder App Instructions](#fastapi-litautoencoder-app-instructions)
  - [General FastAPI request options](#general-fastapi-request-options)
  - [Development in Dev Container](#development-in-dev-container)
  - [Production](#production)

## General FastAPI request options

- Get docs of the request options of the FastAPI app:
  - Dev: `curl -X GET http://localhost:8000/docs`
  - Prod: `curl -X GET http://0.0.0.0:8000/docs`
- Welcome root request of the FastAPI app, providing an app description:
  - Dev: `curl -X GET http://localhost:8000/`
  - Prod: `curl -X GET http://0.0.0.0:8000/`

## Development in Dev Container

- Run the server: `uv run /workspace/demo.py`
- Test the endpoint with curl, copy code and run in the terminal:  

```bash
curl -X POST http://localhost:8000/train \
curl -X POST http://localhost:8000/embed -H "Content-Type: application/json" -d '{"n_fake_images": 1}'
```

## Production

- Build the docker image and start a container; `docker-compose up --build`
- Test the endpoint with curl, copy code and run in the terminal:  

```bash
curl -X POST http://0.0.0.0:8000/train \
curl -X POST http://0.0.0.0:8000/embed -H "Content-Type: application/json" -d '{"n_fake_images": 4}'
```
