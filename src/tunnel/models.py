from datetime import datetime

from src.database import Model, Mapped, DateTime, mapped_column

import uuid


class Tunnel(Model):
    __tablename__ = "tunnels"
    id: Mapped[str] = mapped_column(
        primary_key=True, 
        default=lambda: str(uuid.uuid4())
    )
    target_url: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.utcnow()
    )