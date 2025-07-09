from pydantic import BaseModel, AnyHttpUrl


class NewTunnelRequest(BaseModel):
    target_url: AnyHttpUrl


class TunnelOut(BaseModel):
    id: str
    url: str = "http://domain.com/hook/{id}"
