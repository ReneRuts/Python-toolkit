import os
import cv2
import base64
from stegano import lsb
from pathlib import Path
from time import sleep
from util import print_feature_header

def hide_data_in_image():
    OUTPUT_DIR = Path("output/data_image_hider")

    if not OUTPUT_DIR.exists():
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print("[Info] Getting ready to hide data...")

    image_input = input("Enter the image path to hide data in: ").strip()
    image_path = Path(image_input)

    if not image_path.is_file():
        print("[Error] The image file does not exist.")
        return

    data_to_hide = input("Enter the data you want to hide in the image: ").strip()

    # Hide data using LSB (Least Significant Bit) encoding
    output_image_path = OUTPUT_DIR / f"hidden_{image_path.name}"
    print("[Info] Hiding data in the image...")
    sleep(2)
    lsb.hide(str(image_path), data_to_hide).save(output_image_path)

    print(f"[Info] Data successfully hidden. Saved to {output_image_path}")

    view_image = input("Would you like to view the image? (y/n): ").strip().lower()
    if view_image == "y":
        image = cv2.imread(str(output_image_path))
        cv2.imshow("Hidden Data Image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def extract_data_from_image():
    print("[Info] Extracting data from image...")

    image_input = input("Enter the image path with hidden data: ").strip()
    image_path = Path(image_input)

    if not image_path.is_file():
        print("[Error] The image file does not exist.")
        return

    hidden_data = lsb.reveal(str(image_path))

    if hidden_data:
        print(f"[Info] Extracted Data: {hidden_data}")
    else:
        print("[Error] No hidden data found in this image.")

def encode_data_in_base64():
    print("[Info] Encoding data in Base64...")

    data = input("Enter the data to encode: ").strip()

    encoded_data = base64.b64encode(data.encode('utf-8')).decode('utf-8')

    print(f"[Info] Encoded Data: {encoded_data}")
    return encoded_data

def decode_data_from_base64():
    print("[Info] Decoding Base64 data...")

    encoded_data = input("Enter the Base64 encoded data: ").strip()

    try:
        decoded_data = base64.b64decode(encoded_data).decode('utf-8')
        print(f"[Info] Decoded Data: {decoded_data}")
    except Exception as e:
        print(f"[Error] Failed to decode Base64 data: {e}")

def display_info():
    print_feature_header("Data -> Image Hider")
    print("This feature allows you to hide data within an image using LSB (Least Significant Bit) encoding.")
    print("You can also extract the hidden data from the image and encode/decode data in Base64 format.")
    print("This is useful for steganography, where you want to conceal data within an image file.")
    print("-" * 40)
    input("Press Enter to continue...")

def main():
    while True:
        print_feature_header("Data -> Image Hider")
        print("0. Get info about this feature")
        print("1. Hide data in image")
        print("2. Extract data from image")
        print("3. Encode data in Base64")
        print("4. Decode Base64 data")
        print("5. Return to Main Menu")
        print("6. Exit")

        choice = input("Select an option (0-6): ").strip()

        if choice == "0":
            display_info()
        elif choice == "1":
            hide_data_in_image()
        elif choice == "2":
            extract_data_from_image()
        elif choice == "3":
            encode_data_in_base64()
        elif choice == "4":
            decode_data_from_base64()
        elif choice == "5":
            print("\nReturning to Main Menu...\n")
            return
        elif choice == "6":
            print("Exiting program. Goodbye!")
            exit(0)
        else:
            print("[Error] Invalid option. Please try again!")

if __name__ == "__main__":
    main()
