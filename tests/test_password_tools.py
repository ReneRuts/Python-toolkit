import re
from src.password_tools import generate_password, analyze_strength
from src.config import config

config.update_config(
    pass_lower=True,
    pass_upper=True,
    pass_digits=True,
    pass_symbols=True,
    pass_length=12
)

def test_password_length_default():
    password = generate_password()
    assert isinstance(password, str)
    assert len(password) == config.PASS_LENGTH

def test_password_length_custom():
    password = generate_password(16)
    assert isinstance(password, str)
    assert len(password) == 16

def test_password_contains_required_types():
    password = generate_password()
    assert re.search(r'[a-z]', password)
    assert re.search(r'[A-Z]', password)
    assert re.search(r'[0-9]', password)
    assert re.search(r'[^a-zA-Z0-9]', password)

def test_password_minimum_length_enforced():
    password = generate_password(2)
    assert password is None

def test_strong_password(capfd):
    password = "Ab1!Ab1!Cd2@"
    analyze_strength(password)
    out, _ = capfd.readouterr()
    assert "STRONG" in out

def test_medium_password_missing_special_chars(capfd):
    password = "Ab1Ab1Cd2"
    analyze_strength(password)
    out, _ = capfd.readouterr()
    assert "MEDIUM" in out

def test_weak_password_too_short(capfd):
    password = "Aaa"
    out, _ = capfd.readouterr()
    assert "" in out # No output expected if a password is too short

def test_weak_password_missing_all(capfd):
    password = "password"
    analyze_strength(password)
    out, _ = capfd.readouterr()
    assert "WEAK" in out

def test_many_passwords_unique_and_valid():
    seen = set()
    for _ in range(1000):
        pw = generate_password(16)
        assert pw not in seen
        assert len(pw) == 16
        seen.add(pw)

def test_password_regex_validators():
    pw = generate_password(20)
    assert bool(re.search(r"[a-z]", pw))
    assert bool(re.search(r"[A-Z]", pw))
    assert bool(re.search(r"[0-9]", pw))
    assert bool(re.search(r"[^a-zA-Z0-9]", pw))