import array
from PIL import Image
import numpy as np
from load_image import ft_load


def ft_invert(array) -> array:
    """Invert the colors of the image."""
    # f a pixel value is x, its inverted value should be 255 - x.
    # For example, if a pixel value is 100, its inverted value should be 155
    # If a pixel value is 0 (black), its inverted value should be 255 (white)
    iverted_image = 255 - array  # broadcasting is used here
    Image.fromarray(iverted_image).show()
    return iverted_image


def ft_red(array) -> array:
    """Return an array of pixels with red color."""
    red_image = array.copy()
    # set the green and blue channels to 0
    red_image[:, :, 1] = 0
    red_image[:, :, 2] = 0
    Image.fromarray(red_image).show()
    return red_image


def ft_green(array) -> array:
    """Return an array of pixels with green color."""
    green_image = array.copy()
    # set the red and blue channels to 0
    green_image[:, :, 0] = 0
    green_image[:, :, 2] = 0
    Image.fromarray(green_image).show()
    return green_image


def ft_blue(array) -> array:
    bleu_image = array.copy()
    # set the red and green channels to 0
    bleu_image[:, :, 0] = 0
    bleu_image[:, :, 1] = 0
    Image.fromarray(bleu_image).show()
    return bleu_image


def ft_grey(array) -> array:
    """Return an array of pixels with grey color."""
    # The grey value of a pixel is the average of the red, green,
    # and blue values of the pixel.
    img = array.copy()
    red_channel = img[:, :, 0] / 3
    green_channel = img[:, :, 1] / 3
    blue_channel = img[:, :, 2] / 3
    # sum the three channels
    grey_channel = red_channel + green_channel + blue_channel
    # convert the image to uint8
    Image.fromarray(grey_channel.astype(np.uint8)).show()
    return grey_channel


def main():
    array = ft_load("landscape.jpg")
    ft_invert(array)
    ft_red(array)
    ft_green(array)
    ft_blue(array)
    ft_grey(array)
    print(ft_invert.__doc__)
    print(ft_red.__doc__)
    print(ft_green.__doc__)
    print(ft_blue.__doc__)
    print(ft_grey.__doc__)


if __name__ == "__main__":
    main()
