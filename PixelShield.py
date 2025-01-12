from PIL import Image
import numpy as np

def encrypt_image(image_path, output_path, key):
    """Encrypts an image using a simple mathematical operation on pixel values."""
    # Open the image
    img = Image.open(image_path)
    img_array = np.array(img)

    # Apply encryption (example: add key to pixel values)
    encrypted_array = (img_array + key) % 256  # Modulo to ensure values stay in range
    encrypted_image = Image.fromarray(encrypted_array.astype(np.uint8))

    # Save the encrypted image
    encrypted_image.save(output_path)
    print(f"Image encrypted and saved as {output_path}")


def decrypt_image(encrypted_path, output_path, key):
    """Decrypts an encrypted image by reversing the encryption operation."""
    # Open the encrypted image
    img = Image.open(encrypted_path)
    img_array = np.array(img)

    # Reverse the encryption (example: subtract the key)
    decrypted_array = (img_array - key) % 256
    decrypted_image = Image.fromarray(decrypted_array.astype(np.uint8))

    # Save the decrypted image
    decrypted_image.save(output_path)
    print(f"Image decrypted and saved as {output_path}")


# Menu-driven interface
def main():
    print("Image Encryption and Decryption Tool")
    print("1. Encrypt Image")
    print("2. Decrypt Image")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        image_path = input("Enter the path to the image to encrypt: ")
        output_path = input("Enter the path to save the encrypted image: ")
        key = int(input("Enter an encryption key (integer): "))
        encrypt_image(image_path, output_path, key)
    elif choice == "2":
        encrypted_path = input("Enter the path to the encrypted image: ")
        output_path = input("Enter the path to save the decrypted image: ")
        key = int(input("Enter the decryption key (integer): "))
        decrypt_image(encrypted_path, output_path, key)
    elif choice == "3":
        print("Exiting...")
    else:
        print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
