import numpy as np
from load_image import ft_load
import matplotlib.pyplot as plt


def zoom(image_arr: np.ndarray, zoom_factor: int):
    """zoom

    Args:
        image_arr (np.ndarray): numpy ndarray of image data
        zoom_factor (int): factor to zoom in to picture by
    displays grayscale zoomed in image and prints image data
    to terminal.
    """

    if zoom_factor < 1:
        raise ValueError("zoom factor must be greater than 0")

    zx = image_arr.shape[0] // zoom_factor
    zy = image_arr.shape[1] // zoom_factor
    cropped_arr = image_arr[zx:-zx, zy:-zy, 0:1]
    reshaped = cropped_arr.reshape(cropped_arr.shape[0], cropped_arr.shape[1])
    print("New shape after slicing: ", cropped_arr.shape, "or", reshaped.shape)
    print(cropped_arr)
    # display
    plt.imshow(cropped_arr, cmap='gray')
    plt.show()


def main():
    """main
    Loads the 'animal.jpeg' and zooms into it by a factor of 3.
    Image data info will be printed to terminal and image will be displayed.
    """
    try:
        image_data = ft_load("animal.jpeg")
        zoom(image_data, 3)
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
