from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from core.config import settings
# from apis.general_pages.route_homepage import general_pages_router
from apis.base import api_router
from db.session import engine
from db.base import Base


def include_router(apirouter_app):
    apirouter_app.include_router(api_router)


def configure_static(app):
    app.mount("/static", StaticFiles(directory="static"), name='static')


def create_tables():
    print('creating tables')
    Base.metadata.create_all(bind=engine)


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME,
                  version=settings.PROJECT_VERSION)
    include_router(app)
    configure_static(app)
    # create_tables()
    return app


app = start_application()

# app = FastAPI()


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
#
#
# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}
