from PIL import Image
import os

def hide_text_in_image(input_image_path, output_image_path, secret_message, key):
    image = Image.open(input_image_path)
    binary_secret_message = ''.join(format(ord(char), '08b') for char in secret_message)
    if len(binary_secret_message) > image.width * image.height * 3:
        raise ValueError("Message too large to hide in image")

    index = 0
    for i in range(image.width):
        for j in range(image.height):
            r, g, b = image.getpixel((i, j))

            if index < len(binary_secret_message):
                image.putpixel((i, j), (r, g, int(format(b, '08b')[:-1] + binary_secret_message[index], 2)))
                index += 1

    image.save(output_image_path)

def extract_text_from_image(input_image_path, key):
    image = Image.open(input_image_path)
    binary_secret_message = ""
    for i in range(image.width):
        for j in range(image.height):
            r, g, b = image.getpixel((i, j))
            binary_secret_message += format(b, '08b')[-1]

    secret_message = "".join(chr(int(binary_secret_message[i:i+8], 2)) for i in range(0, len(binary_secret_message), 8))
    return secret_message

def main():
    input_image_path = input("Enter the input image path: ")
    output_image_path = input("Enter the output image path: ")
    secret_message = input("Enter the message to hide: ")
    epassword = input("Enter the password: ")
    
    hide_text_in_image(input_image_path, output_image_path, secret_message, epassword)
    
    input_image_path = input("Enter the input image path to extract message from: ")
    dpassword = input("Enter the password to decrypt the message: ")
    decrypted_message = extract_text_from_image(input_image_path, dpassword)
    if epassword==dpassword:
        print("Decrypted message: ", secret_message)
    else:
        print("Password incorrect !!!!")
        print("Thanks for exicuting")

if __name__ == "__main__":
    main()
