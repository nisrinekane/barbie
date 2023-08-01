from PIL import Image, ImageDraw

def generate_img(individual):
    img = Image.new('1', (100, 100))
    draw = ImageDraw.Draw(img)

    for point in individual:
        x = int(point[0] * 100)
        y = int(point[1] * 100)
        draw.point((x,y), fill='pink')

        return img


def calculate_difference(img1, img2):
    diff = 0
    for i in range(img1.width):
        for j in range(img1.height):
            diff += abs(img1.getpixel((u, j)) - img2.getpixel((i, j)))
    return diff