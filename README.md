# image-hide
Steganography is the practice of concealing a message, file, image, or video within another message, file, image, or video in order to hide the existence of the concealed information.
Image Steganography: Concealing information within digital images by subtly modifying the pixel values. This can involve hiding data in the least significant bits of the image, using specific patterns, or altering the color values.
Objective:
	The project aims to demonstrate a basic form of steganography, specifically hiding a text message within the pixels of an image.
	 
I used a method of Hiding a text message within the pixels of an image is a form of steganography.

* Here's a step-by-step explanation of how text is typically hidden within the pixels of an image :

1.Binary Representation of Text:
The text message is first converted into binary form. Each character is represented by a sequence of 8 bits (one byte).

2.Image Pixels:
In a digital image, each pixel is composed of color channels, often represented as red (R), green (G), and blue (B). Each color channel has a value ranging from 0 to 255 in an 8-bit image.

3.Least Significant Bit (LSB) Replacement:
The least significant bit (LSB) is the rightmost bit in a binary representation. In steganography, the LSB of the color channels in the image can be modified without significantly altering the color or appearance to the human eye.

4.Hiding the Text:
The binary representation of the text message is embedded by replacing the LSB of the blue channel in each pixel with the corresponding bit from the binary message.
This is done iteratively for each pixel in the image, spreading the bits of the hidden message across the entire image.

5.Saving the Modified Image:
Once the text message is embedded in the image, the modified image is saved. To the naked eye, the image appears unchanged, but the hidden message is now encoded in the LSB of the blue channel.

6.Extraction of the Hidden Text:
To extract the hidden text, the image is processed pixel by pixel, and the LSB of the blue channel is read. These LSBs are then concatenated to reconstruct the binary representation of the hidden message.The binary message is then converted back to text.

