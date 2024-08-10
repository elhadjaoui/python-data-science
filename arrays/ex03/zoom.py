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
        if not path.lower().endswith(("jpg", "jpeg")):
            raise AssertionError("Only JPG and JPEG formats are supported.")
        with Image.open(path)as img:
            np_img = np.array(img)
            print(f"The shape of image is: {np_img.shape}")
            # print(np_img)
            print(img.size)
            cropped_image = np_img[90:490, 450:850, :]
            cropped_image_pil = Image.fromarray(cropped_image).convert('L')
            cropped_image_np = np.array(cropped_image_pil)
            new_shape = cropped_image_np.reshape(400, 400, 1)
            print(f"The new shape of image is: {new_shape.shape} or ", end="")
            print(f"{cropped_image_pil.size}")
            print(new_shape)
            cropped_image_pil.save("zoomed.jpeg")
            return new_shape.tolist()
    except FileNotFoundError:
        print("The file was not found.")
        return None
    except AssertionError as e:
        print(e)
        return None
    except Exception:
        print("An error occurred.")
        return None


def main():
    path = "animal.jpeg"
    zoom(path)


if __name__ == "__main__":
    main()
