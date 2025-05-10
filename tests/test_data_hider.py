from src.data_hider import encode_text_base64, decode_text_base64, hide_data, extract_hidden_data


def test_encode_base64():
    # Test for encoding data to Base64
    data = "Hello world"
    encoded_data = encode_text_base64(data)
    expected_encoded_data = "SGVsbG8gd29ybGQ="  # Base64 encoding of "Hello world"
    assert encoded_data == expected_encoded_data


def test_decode_base64():
    # Test for decoding Base64 data
    encoded_data = "SGVsbG8gd29ybGQ="  # Base64 encoded "Hello world"
    decoded_data = decode_text_base64(encoded_data)
    assert decoded_data == "Hello world"


def test_invalid_decode_base64():
    # Test for decoding invalid Base64 data
    invalid_data = "invalid_base64_data"
    
    try:
        decode_text_base64(invalid_data)
    except Exception:
        pass  # Exception expected
    else:
        assert False, "Expected an exception for invalid Base64 data"

def test_extract_hidden_data():
    # Test for extracting data
    image_path = "tests\\data_hider_images\\hidden_test_image_with_data.png"  # Dummy path for the image
    
    extracted_data = extract_hidden_data(image_path)
    
    assert extracted_data == "Hello world"

def test_extract_hidden_data_empty_image():
    # Test extracting data from an image without hidden data
    image_path = "tests\\data_hider_images\\test_image_without_data.png"

    try:
        extracted_data = extract_hidden_data(image_path)
        # If no hidden data, it should return None
        assert extracted_data is None
    except IndexError:
        # If an IndexError occurs, it means no data was hidden in the image
        assert True  # Test passes if IndexError is raised
    print("Test Passed: Extract Data from Empty Image")
