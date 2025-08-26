TASKCORE

A modular **task management API** built with **FastAPI** and **SQLModel**.
This project implements a backend service with database integration, RESTful routes and structured project architecture.

## Features
- CRUD operations for tasks (Create, Read, Update, Delete)
- RESTful API Design with HTTP status codes
- SQLite database
- SQLModel for type-safe ORM 
- astAPI for async API endpoints
- Modular architecture with models, database setup, and routes separated
- Interactive dovumentation via Swagger UI ('/docs')

## Project Architecture
**main.py** - application entry point
**database.py** - DB engine, DB initializer, session handler
**task.py** - Task models (ORM)
**task_routes.py** - All Task CRUD endpoints
**task.db** - SQLite database
**README.md**

## Tech Stack 
- **FastAPI** – modern Python web framework for building APIs
- **SQLModel** – ORM built on SQLAlchemy + Pydantic
- **SQLite** – lightweight relational database
- **Uvicorn** – lightning-fast ASGI server

## Getting Started
###1. Clone the repository 
"```bash
git clone https://github.com/<your-username>/taskforge-api.git
cd taskforge-api "

###2.Create virtual environment & install dependencies
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

###3. Run API
uvicorn main:app --reload

###4. Explore the docs
Swagger UI → http://127.0.0.1:8000/docs
