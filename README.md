# Image Encryption and Decryption Tool

This Python tool allows you to encrypt and decrypt images using a simple mathematical operation on pixel values. The encryption is achieved by adding an integer key to the pixel values, and decryption is done by subtracting the same key.

## Requirements
- Python 3.x
- Pillow (PIL) library
- NumPy library

You can install the required libraries using:
```bash
pip install pillow numpy
```

## Usage

Run the script and select the desired option from the menu:
- **Encrypt Image**: Enter the image path, provide an encryption key (integer), and save the encrypted image.
- **Decrypt Image**: Enter the encrypted image path, provide the decryption key (same as encryption key), and save the decrypted image.
- **Exit**: Close the tool.

## Example
```bash
$ python image_encryption_tool.py
```
##Image Encryption and Decryption Tool
1. Encrypt Image
2. Decrypt Image
3. Exit
Enter your choice: 1
Enter the path to the image to encrypt: /path/to/image.jpg
Enter the path to save the encrypted image: /path/to/encrypted_image.jpg
Enter an encryption key (integer): 42
Image encrypted and saved as /path/to/encrypted_image.jpg
## Code Explanation
- **Encrypt**: Adds the key to each pixel's value, wraps around with modulo 256.
- **Decrypt**: Subtracts the key from each pixel's value to recover the original image.

## License
This project is open-source and available under the MIT License.
