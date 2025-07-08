from src.database import AsyncSession

from .models import Tunnel


async def new_tunnel(
    db_session: AsyncSession,
    target_url: str,
) -> Tunnel:
    tunnel = Tunnel(target_url=str(target_url))
    db_session.add(tunnel)
    await db_session.commit()
    return tunnel


async def get_tunnel(
    db_session: AsyncSession,
    id: str,
) -> Tunnel:
    return await db_session.get(Tunnel, id)
    