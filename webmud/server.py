#!/usr/bin/env python

import asyncio
import json
from websockets.server import serve

from .alex_game import handle_message;

async def echo(websocket):
    async for message in websocket:
        message = json.loads(message)
        response = handle_message(message['command'], message['id'])
        await websocket.send(response)

async def run_ws_server():
    async with serve(echo, "", 8080):
        await asyncio.Future()  # run forever


