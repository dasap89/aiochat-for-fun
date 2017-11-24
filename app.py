import asyncio
from aiohttp import web
from routes import routes

loop = asyncio.get_event_loop()

app = web.Application(loop=loop, middlewares=[
    session_middleware(EncryptedCookieStorage(SECRET_KEY)),
    authorize,
    db_handler,
])

for route in routes:
    app.router.add_route(route[0], route[1], route[2], name=route[3])