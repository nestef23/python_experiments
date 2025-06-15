# Simple Uvicorn Docker Project

This is a minimal [FastAPI](https://fastapi.tiangolo.com/) server running inside a Docker container that serves a webpage with a button. Clicking the button sends a request to the server.

## 📦 Features

- Lightweight Python + FastAPI web app
- Dockerized for easy deployment
- Includes a basic HTML page with a button
- Can be deployed via **Docker CLI** or **Ansible playbook**

---

## 🚀 Run with Docker (manual)

Build and run the container manually using Docker:

```bash
docker build -t simple-uvicorn .
docker run -p 8000:8000 simple-uvicorn
```
## 🚀 Run with Docker Compose (manual)
You can also start the app using Docker Compose:

```bash
docker compose up --build
```

## 🚀 Deploy with Ansible
This project supports automated deployment with Ansible using Docker Compose.
- Ensure that ansible is configured correctly, and you can execute playbooks on the target host(s).
- Populate the inventory file correctly
- This playbook works on Ubuntu currently.
```
ansible-playbook -i inventory.ini playbook.yaml
```
