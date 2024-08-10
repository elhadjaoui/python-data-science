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
            print(np_img)
            np_img.reshape(400, 400, 1)
            print(f"The shape of image is: {np_img.shape}")
            img.fromarray(np_img).show()
            return np_img.tolist()
    except FileNotFoundError:
        print("The file was not found.")
        return None


def main():
    path = "animal.jpeg"
    zoom(path)


if __name__ == "__main__":
    main()
