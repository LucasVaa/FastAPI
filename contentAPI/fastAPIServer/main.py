import os
import sys
sys.path.append(os.pardir)
from fastapi import FastAPI

from routers import admin, app, node


app_admin = FastAPI()

app_admin.include_router(admin.router)

app_app = FastAPI()

app_app.include_router(app.router)

app_node = FastAPI()

app_node.include_router(node.router)