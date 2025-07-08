from fastapi import APIRouter, Request, Response, HTTPException
from httpx import AsyncClient

from src.database import DbSession
from src.tunnel.service import get_tunnel


router = APIRouter()


@router.api_route(
    "/hook/{tunnel_id}",
    methods=["GET", "POST", "PUT", "PATCH", "DELETE"],
    tags=["hook"]
)
@router.api_route(
    "/hook/{tunnel_id}/{path:path}",
    methods=["GET", "POST", "PUT", "PATCH", "DELETE"],
    tags=["hook"]
)
async def hook_handler(
    tunnel_id: str,
    request: Request,
    db_session: DbSession,
    path: str = None,
):
    tunnel = await get_tunnel(db_session, tunnel_id)
    if not tunnel:
        raise HTTPException(
            status_code=404,
            detail="Tunnel not found"
        )

    url = tunnel.target_url.rstrip("/") + "/" + path if path else tunnel.target_url
    method = request.method
    body = await request.body()
    headers = dict(request.headers)

    async with AsyncClient() as client:
        try:
            response = await client.request(
                method=method,
                url=url,
                headers=headers,
                content=body,
                timeout=10.0,
            )
        except Exception as e:
            raise HTTPException(
                status_code=502,
                detail=f"Forwarding error: {str(e)}"
            )
    return Response(
        content=response.content,
        status_code=response.status_code,
        headers=dict(response.headers)
    )