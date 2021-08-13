

from pydantic import BaseModel
from .core import app


class GenericMessage(BaseModel):
    message: str


@app.post("/echo")
async def echo(message: GenericMessage):
    return {'message': message.message}
