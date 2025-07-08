from fastapi import FastAPI

from src.database import create_tables

app = FastAPI()


from src.tunnel.router import router as tunnel_router
app.include_router(tunnel_router)
from src.hook.router import router as hook_router
app.include_router(hook_router)

@app.on_event("startup")
async def startup():
    await create_tables()