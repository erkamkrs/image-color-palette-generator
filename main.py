import math
import PIL
import extcolors
import urllib.request
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
from matplotlib import gridspec




def inspect_image(image_path):
    image = fetch_image(image_path)
    colours = get_colours(image)
    colour_palette = render_colour_palette(colours)
    overlay_palette(image, colour_palette)

def fetch_image(image_path):
    urllib.request.urlretrieve(image_path, "img")
    image = PIL.Image.open("img")
    return image


def get_colours(image):
    tolerance = 32
    limit = 24
    colours, pixel_count = extcolors.extract_from_image(image, tolerance, limit)
    return colours

def overlay_palette(image, colour_palette):
    fig = plt.figure(figsize=(25, 35), facecolor="None", edgecolor="k", dpi=55, num=None)
    ncol = 1
    nrow = 2
    gridsspec = gridspec.GridSpec(nrow, ncol, wspace=0.0, hspace=0.0)
    fig.add_subplot(2,1,1)
    plt.imshow(image, interpolation="nearest")
    plt.axis("off")
    fig.add_subplot(1,2,2)
    plt.imshow(colour_palette, interpolation="nearest")
    plt.axis("off")
    plt.subplots_adjust(wspace=0, bottom=0, hspace=0)
    plt.show(block=True)

def render_colour_palette(colours):
    columns = 6
    size = 100
    width = int(min(len(colours), columns * size))
    height = int((math.floor(len(colours)/ columns) + 1) * size)
    result = Image.new("RGBA", (width, height), (0,0,0,0))
    canvas = ImageDraw.Draw(result)
    for index, colour in enumerate(colours):
        x = int((index % columns) * size)
        y = int(math.floor(index / columns) * size)
        canvas.rectangle([(x, y), (x + size - 1, y + size -1)], fill=colour[0])
    return result

image_url = 'https://www.google.com/url?sa=i&url=https%3A%2F%2Ftwitter.com%2Ferkamkiris&psig=AOvVaw12vCAdlXwqYBxVYM_Fwgm8&ust=1676037953464000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCIjf34jOiP0CFQAAAAAdAAAAABAE'
inspect_image(image_url)
