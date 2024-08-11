from PIL import Image
import numpy as np
import load_image as li


def rotate(np_img: np.array):
    """Return a list of lists of pixels.
    The image is cropped to 400x400 pixels.
    and converted to grayscale.
    args:
        np_img: np.array - array of pixels
    returns:
        list - list of lists of pixels
    """
    # Crop the image to 400x400 pixels
    cropped_image = np_img[90:490, 450:850, :]
    # Convert the image to grayscale
    cropped_image_pil = Image.fromarray(cropped_image).convert('L')
    # Convert the image to a numpy array
    cropped_image_np = np.array(cropped_image_pil)
    # Reshape the image to 400x400 pixels
    new_shape = cropped_image_np.reshape(400, 400, 1)
    # get the shape of the image height, width, channels
    height, width, _ = new_shape.shape
    # Remove the channel dimension to get a 2D image
    image_2d = np.squeeze(new_shape, axis=2)
    # initialize a new image with the same shape as the original image
    rotated_image = np.zeros((width, height), dtype=new_shape.dtype)
    # Rotate the image by 90 degrees
    # swap the height and width of the image to rotate it by 90 degrees
    for i in range(height):
        rotated_image[:, i] = image_2d[i, :]
    print(f"The shape after transpose : {rotated_image.shape}")
    print(rotated_image)
    rotated_image_pil = Image.fromarray(rotated_image)
    rotated_image_pil.save("rotated.jpeg")


def main():
    path = "animal.jpeg"
    rotate(li.load_image(path))


if __name__ == "__main__":
    main()
