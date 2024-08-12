from PIL import Image
import numpy as np


def ft_load(path: str) -> np.array:
    """Return an array of pixels.
    args:
        path: str - path to the image
    returns:
        np.array - array of pixels
        """
    try:
        if not path.lower().endswith(("jpg", "jpeg")):
            raise AssertionError("Only JPG and JPEG formats are supported.")
        with Image.open(path)as img:
            np_img = np.array(img)
            print(f"The shape of image is: {np_img.shape}")
            print(np_img)
            return np_img
    except FileNotFoundError:
        print("The file was not found.")
        exit(1)
    except AssertionError as e:
        print(e)
        exit(1)
    except Exception:
        print("An error occurred.")
        exit(1)


def main():
    path = "animal.jpeg"
    ft_load(path)


if __name__ == "__main__":
    main()
