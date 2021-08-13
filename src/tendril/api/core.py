

from fastapi import FastAPI
app = FastAPI()

from tendril.utils.versions import get_versions


@app.get("/core/versions")
async def versions():
    return {k: v for (k, v) in get_versions('tendril')}
