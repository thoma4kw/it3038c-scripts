pip install Pillow

from PIL import Image, ImageFilter, ImageDraw, ImageFont

# Usage 1: Open and Display an Image
image = Image.open("example.jpg")
image.show()

# Usage 2: Apply a Filter to the Image
blurred_image = image.filter(ImageFilter.BLUR)
blurred_image.show()

# Usage 3: Add Text to an Image
draw = ImageDraw.Draw(image)
font = ImageFont.truetype("arial.ttf", 36)  # Change the font and size as needed
text = "Hello, Pillow!"
draw.text((50, 50), text, fill="red", font=font)
image.show()

# Save the modified image
image.save("modified_image.jpg")
