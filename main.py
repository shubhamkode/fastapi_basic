import fastapi as _fastapi
import uvicorn as _server

import src.routes.routes as _routes 

app = _fastapi.FastAPI()

app.include_router(_routes.router)


if __name__ == "__main__":
    _server.run("main:app", reload=True)
