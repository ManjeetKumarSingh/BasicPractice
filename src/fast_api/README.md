#### Author : Manjeet Kumar

### About the FastAPI

* The FastAPI framework is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.

* FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.

* It's designed to help you build APIs with:

### Basic requirements for having hands on fastApi 

```
FastAPI is a modern Python framework for building REST APIs.

It is built primarily on:

* Starlette → web framework / HTTP handling
* Pydantic → validation and serialization
* Uvicorn → ASGI server
* Python type hints → validation + automatic API documentation

```

### For installing these we need 
* `python -m pip install uvicorn`
* `python -m pip install fastapi`
* `python -m pip install pydantic`
* `python -m pip install sqlalchemy`

### For running the code we need to use the command 
* `uvicorn main:app --reload`
* `main` is the name of the file
* `app` is the name of the variable in the file

### Basic architecture of the fastApi project is like this
```
Client
   |
   v
API Gateway / Load Balancer
   |
   v
FastAPI
   |
   +---- Middleware
   |
   +---- Authentication
   |
   +---- Router
   |
   +---- Service Layer
   |
   +---- Repository
   |
   +---- Database

   ```

### For running the fastapi , the command is 

   ```
   uvicorn main_api:app --reload
   ```


   ### Swagger Docuentations for the fastApi project 

   * 
   ```
   http://127.0.0.1:8000/docs

   http://127.0.0.1:8000/redoc

   http://127.0.0.1:8000/openapi.json

   ```