# Simple Uvicorn Docker Project

This is a minimal FastAPI server running inside a Docker container that serves a webpage with a button. Clicking the button sends a request to the server.

## Run

```bash
docker build -t simple-uvicorn .
docker run -p 8000:8000 simple-uvicorn
