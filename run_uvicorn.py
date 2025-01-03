import os, uvicorn

uvicorn.run(
    "server:app",
    host="0.0.0.0",
    port=7330,
    ssl_keyfile=os.path.join(os.path.dirname(__file__), 'key', 'origin.key'),
    ssl_certfile=os.path.join(os.path.dirname(__file__), 'key', 'origin.pem')
)