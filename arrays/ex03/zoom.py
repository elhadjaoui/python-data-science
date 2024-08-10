from PIL import Image
import numpy as np


def zoom(path: str) -> list:
    """Return a list of lists of pixels.
    args:
        img: list - list of lists of pixels
        factor: int - factor to zoom the image
    returns:
        list - list of lists of pixels
    """
    try:
        with Image.open(path)as img:
            np_img = np.array(img)
            print(f"The shape of image is: {np_img.shape}")
            # print(np_img)
            # (width, height) = img.size
            # print(f"Width: {width}, Height: {height}")
            # crop image
            # new_image = img.crop((width - 350, height - 350, 350, 350)).show()
            cropped_image = np_img[:600, :600, :]
            # new_image = img.resize((700, 700)).show()
            # new_image.save("animall.jpeg")
            # print(f"The shape of image is: {np_img.shape}")
            Image.fromarray(cropped_image).convert('L').show()
            # return np_img.tolist()
    except FileNotFoundError:
        print("The file was not found.")
        return None


def main():
    path = "animal.jpeg"
    zoom(path)


if __name__ == "__main__":
    main()
