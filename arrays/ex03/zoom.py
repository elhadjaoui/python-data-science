from PIL import Image
import numpy as np
import load_image as li


def zoom(np_img: np.array) -> list:
    """Return a list of lists of pixels.
    The image is cropped to 400x400 pixels.
    and converted to grayscale.
    args:
        np_img: np.array - array of pixels
    returns:
        list - list of lists of pixels
    """
    cropped_image = np_img[90:490, 450:850, :]
    cropped_image_pil = Image.fromarray(cropped_image).convert('L')
    cropped_image_np = np.array(cropped_image_pil)
    new_shape = cropped_image_np.reshape(400, 400, 1)
    print(f"The new shape of image is: {new_shape.shape} or ", end="")
    print(f"{cropped_image_pil.size}")
    print(new_shape)
    cropped_image_pil.save("zoomed.jpeg")
    return new_shape.tolist()


def main():
    path = "animal.jpeg"
    zoom(li.load_image(path))


if __name__ == "__main__":
    main()
