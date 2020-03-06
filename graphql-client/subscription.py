import json
import uuid

import websockets

from .utils import _get_updated_headers

GRAPHQL_PROTOCOL = "graphql-ws"


class Subscription:
    def __init__(self, parent, query, variables=None, headers=None):
        self._id = uuid.uuid4().hex
        self.endpoint = parent.endpoint
        self.variables = variables
        self.query = query
        self.headers = _get_updated_headers(parent.headers, headers)
        self.is_running = False

    async def _con_init(self):
        self._conn = await websockets.connect(
            self.endpoint, subprotocols=[GRAPHQL_PROTOCOL]
        )
        payload = {"type": "connection_init"}
        await self._conn.send(json.dumps(payload))
        await self._conn.recv()

    async def listen(self):
        while self.is_running:
            resp = await self._conn.recv()
            try:
                resp = json.loads(resp)
            except:
                # TODO need to log the response
                continue

            if resp.get("type") == "ka":
                continue

            yield resp.get("payload", {})

    async def start(self):
        await self._con_init()
        payload = {
            "query": self.query,
            "variables": self.variables,
            "headers": self.headers,
        }
        message = {"id": self._id, "type": "start", "payload": payload}
        await self._conn.send(json.dumps(message))
        res = await self._conn.recv()
        print("after start %s" % res)
        self.is_running = True

    async def stop(self):
        payload = {"id": self._id, "type": "stop"}
        self.is_running = False
        await self._conn.send(json.dumps(payload))
        return self._conn.recv()
