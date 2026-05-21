import json
from http.client import HTTPConnection
from threading import Thread

from gamma_labyrinth.server import make_server, smoke_payload


def test_smoke_payload_truth_safe():
    payload = smoke_payload()
    assert payload["ok"] is True
    assert payload["truth_status"] == "truth_safe_unverified"
    assert payload["state"]["truth_bearing_run"] is False


def test_server_health_endpoint():
    server = make_server("127.0.0.1", 0)
    port = server.server_address[1]
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        conn = HTTPConnection("127.0.0.1", port, timeout=5)
        conn.request("GET", "/health")
        response = conn.getresponse()
        body = json.loads(response.read().decode("utf-8"))
        assert response.status == 200
        assert body["ok"] is True
        assert body["truth_status"] == "truth_safe_unverified"
    finally:
        server.shutdown()
        thread.join(timeout=5)
