from fastapi import APIRouter

from src.database import DbSession
from .schemas import NewTunnelRequest, TunnelOut
from .service import new_tunnel
from .models import Tunnel


router = APIRouter()


@router.post(
    "/tunnels",
    tags=["api", "tunnel"],
    status_code=201,
    response_model=TunnelOut,
)
async def new_tunnel_handler(
    data: NewTunnelRequest,
    db_session: DbSession,
):
    target_url = data.target_url
    tunnel = await new_tunnel(db_session, target_url)
    print(str(tunnel.target_url) + ','+ tunnel.id)
    return {
        "url": f"/hook/{tunnel.id}"
    }