from src.service_comparator import check_port

# This test checks if the port that's defined is open or not. (Change the port to a known open port)
def test_check_port_known_open():
    result = check_port("127.0.0.1", 80)
    assert result is True

# This test checks if a high-numbered port that's likely closed
def test_check_port_known_closed():
    result = check_port("127.0.0.1", 65534)
    assert result is False

def test_check_port_invalid_host():
    result = check_port("invalid.hostname.local", 22)
    assert result is False

def test_check_port_invalid_ip_format():
    result = check_port("999.999.999.999", 22)
    assert result is False
