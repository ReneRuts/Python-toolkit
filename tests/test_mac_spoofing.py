from src.mac_spoofing import get_current_mac, generate_random_mac, is_valid_mac, check_os
import os
TEST_INTERFACE = "lo" if os.name != 'nt' else "Ethernet"

def test_check_os():
    result = check_os()
    assert result in [True, False]

def test_is_valid_mac_invalid():
    assert not is_valid_mac("ZZ:ZZ:ZZ:ZZ:ZZ:ZZ")
    assert not is_valid_mac("12345")
    assert not is_valid_mac("AA:BB:CC:DD:EE")
    assert not is_valid_mac("")

def test_generate_random_mac():
    mac = generate_random_mac()
    assert isinstance(mac, str)
    assert is_valid_mac(mac)

def test_get_current_mac_format():
    mac = get_current_mac(TEST_INTERFACE)
    if mac:
        assert is_valid_mac(mac)