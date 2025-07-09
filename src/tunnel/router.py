from fastapi import APIRouter, HTTPException

from src.database import DbSession
from .schemas import NewTunnelRequest, TunnelOut
from .service import new_tunnel, get_tunnel, delete_tunnel
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


@router.delete(
    "/tunnels/{tunnel_id}",
    status_code=204,
    response_model=str,
)
async def delete_tunnel_handler(
    tunnel_id: str,
    db_session: DbSession,
):
    tunnel_exists = await get_tunnel(db_session, tunnel_id)
    if not tunnel_exists:
        raise HTTPException(
            status_code=404,
            detail="Tunnel not found"
        )
    await delete_tunnel(db_session, tunnel_id)
    