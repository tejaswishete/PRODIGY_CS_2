from PIL import Image 
import random

def encrypt_image(image_path, key, output_path):
    # Open the image and convert it to RGB mode
    img = Image.open(image_path).convert('RGB')
    pixels = list(img.getdata())
    
    encrypted_pixels = []
    for i in range(len(pixels)):
        r, g, b = pixels[i]  # Unpack the RGB values
        # Encrypt r, g, b using the key (assuming some encryption logic)
        encrypted_r = r ^ key  # Example: XOR encryption
        encrypted_g = g ^ key
        encrypted_b = b ^ key
        encrypted_pixels.append((encrypted_r, encrypted_g, encrypted_b))

    # Create a new image with the encrypted pixels
    encrypted_img = Image.new(img.mode, img.size)
    encrypted_img.putdata(encrypted_pixels)
    encrypted_img.save(output_path)
    print(f"Encrypted image saved as {output_path}")

def decrypt_image(image_path, key, output_path):
    # Open the image
    img = Image.open(image_path)
    pixels = list(img.getdata())
    width, height = img.size

    # Seed random number generator with the key
    random.seed(key)

    # Generate the same shuffled indices
    indices = list(range(len(pixels)))
    random.shuffle(indices)
    
    # Reverse the mathematical operation applied during encryption
    decrypted_pixels = [None] * len(pixels)
    for i, pixel in zip(indices, pixels):
        r, g, b = pixel
        r = (r - key) % 256
        g = (g - key) % 256
        b = (b - key) % 256
        decrypted_pixels[i] = (r, g, b)

    # Create a new image with the decrypted pixels
    decrypted_img = Image.new(img.mode, img.size)
    decrypted_img.putdata(decrypted_pixels)
    decrypted_img.save(output_path)
    print(f"Decrypted image saved as {output_path}")

# Example usage:
key = 123  # Encryption key (must be the same for encryption and decryption)
encrypt_image('input_image.png', key, 'encrypted_image.png')
decrypt_image('encrypted_image.png', key, 'decrypted_image.png')