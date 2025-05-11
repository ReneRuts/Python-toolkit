from src.mini_ddos import send_packet, send_packets_threaded
from src.config import config

def test_send_packet_runs_without_exception():
    result = send_packet()
    assert result is None or isinstance(result, str)

def test_send_packets_threaded_runs():
    assert send_packets_threaded() is None

def test_send_packet_success_to_localhost():
    assert config.TARGET_HOST == "127.0.0.1" or config.TARGET_HOST == "localhost"
    assert config.TARGET_PORT == 80
    result = send_packet()
    assert result is None