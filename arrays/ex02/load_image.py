from PIL import Image
import numpy as np


def ft_load(path: str) -> list:
    """Return a list of lists of pixels.
    args:
        path: str - path to the image
    returns:
        list - list of lists of pixels
    """
    try:
        if path.split(".")[-1] not in ["jpg", "jpeg"]:
            print("only jpg and jpeg files are supported.")
            return None
        with Image.open(path)as img:
            np_img = np.array(img)
            print(f"The shape of image is: {np_img.shape}")
            print(np_img)
            return np_img.tolist()
    except FileNotFoundError:
        print("The file was not found.")
        return None


def main():
    path = "landscape.jpg"
    ft_load(path)


if __name__ == "__main__":
    main()
