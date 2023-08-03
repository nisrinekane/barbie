from PIL import Image, ImageDraw
from config import IMG_WIDTH, IMG_HEIGHT, POINT_COUNT

def generate_img(individual):
    img = Image.new('RGB', (IMG_WIDTH, IMG_HEIGHT), "black") # this creates black canvas
    pixels = img.load() 

    for i in range(img.width):
        for j in range(img.height):
            # xxtract color from individual
            color = tuple(int(255 * individual[(i * img.width + j) % POINT_COUNT][k]) for k in range(3))
            pixels[i, j] = color

    return img

def calculate_difference(img1, img2):
    diff = 0
    for i in range(img1.width):
        for j in range(img1.height):
            pixel1 = img1.getpixel((i, j))
            pixel2 = img2.getpixel((i, j))
            for k in range(3):  # for each RGB component
                diff += (pixel1[k] - pixel2[k]) ** 2  # square the difference
    return diff

