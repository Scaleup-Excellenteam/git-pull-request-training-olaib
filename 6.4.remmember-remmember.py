from PIL import Image

# IMAGE_PATH = 'source/code.png'
IMAGE_PATH = 'source/code.png'


def decoding_msg_from_img(img_path):
    # Open the image
    img = Image.open(img_path)
    # Get the width and height of the image
    width, height = img.size[:2]
    pixels = img.load()
    return "".join([chr(row) for col in range(width) for row in range(height) if pixels[col, row] == 1])


if __name__ == '__main__':
    print(decoding_msg_from_img(IMAGE_PATH))
