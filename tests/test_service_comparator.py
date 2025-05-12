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

import pytest
from src.service_comparator import display_service_differences

def test_display_service_differences_all_common(capfd):
    mock_data = [
        {
            "host": "192.168.0.1",
            "services": ["nginx.service", "ssh.service", "cron.service"],
            "open_ports": {22: True}
        },
        {
            "host": "192.168.0.2",
            "services": ["nginx.service", "ssh.service", "cron.service"],
            "open_ports": {22: True}
        },
    ]
    display_service_differences(mock_data)
    out, _ = capfd.readouterr()
    assert "There are no differences for the services for all the hosts." in out

def test_display_service_differences_with_differences(capfd):
    mock_data = [
        {
            "host": "host1",
            "services": ["nginx.service", "ssh.service"],
            "open_ports": {}
        },
        {
            "host": "host2",
            "services": ["nginx.service", "docker.service"],
            "open_ports": {}
        },
    ]
    display_service_differences(mock_data)
    out, _ = capfd.readouterr()
    assert "Common services across all hosts" in out
    assert "nginx.service" in out
    assert "ssh.service" in out or "docker.service" in out
    assert "Unique services per host" in out

def test_display_service_differences_insufficient_hosts(capfd):
    mock_data = [
        {
            "host": "host1",
            "services": ["nginx.service", "ssh.service"],
            "open_ports": {}
        }
    ]
    display_service_differences(mock_data)
    out, _ = capfd.readouterr()
    assert "Not enough host data to compare" in out
