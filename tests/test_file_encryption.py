from src.file_encryption import generate_key, load_key, get_key_file_path

def test_generate_key_creates_valid_file():
    # override default path to test file
    test_path = "tests\\file_encryption_files\\file_encryption_key.key"
    def fixed_path():
        return test_path
    import src.file_encryption as sfe
    sfe.get_key_file_path = fixed_path

    generate_key()
    key_bytes = open(test_path, "rb").read()
    assert len(key_bytes) == 44  # Fernet key length is 44 bytes
    assert key_bytes.endswith(b"=")

def test_load_key_returns_correct_data():
    import src.file_encryption as sfe

    # Return the path as a Path object (not a string)
    sfe.get_key_file_path = lambda: sfe.Path("tests/file_encryption_files/file_encryption_key.key")

    key = load_key()
    assert isinstance(key, bytes)
    assert len(key) == 44
