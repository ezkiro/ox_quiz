from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from datetime import datetime
import json
from fastapi_healthcheck import HealthCheckFactory, healthCheckRoute

app = FastAPI()
app.add_api_route('/health', endpoint=healthCheckRoute(factory=HealthCheckFactory()))

connected_users = {}
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.websocket("/ws/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: str):
    await websocket.accept()
    connected_users[user_id] = websocket
    while True:
        try:
            data = await websocket.receive_text()
            print(data)
            for user, user_ws in connected_users.items():
                if user != user_id:
                    await user_ws.send_text(f"Message text was: {data}")
        except WebSocketDisconnect:
            del connected_users[user_id]
            await websocket.close()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
