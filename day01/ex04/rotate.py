import numpy as np
from load_image import ft_load
import matplotlib.pyplot as plt


def rotate(image_arr: np.ndarray):
    """rotate

    Args:
        image_arr (np.ndarray): numpy ndarray of image data
    displays grayscale rotated image and prints image data
    to terminal.
    """

 

    zx = image_arr.shape[0] // 4
    zy = image_arr.shape[1] // 4
    cropped_arr = image_arr[zx:-zx, zy:-zy, 0:1]
    # cropped_arr = cropped_arr
    reshaped = cropped_arr.reshape(cropped_arr.shape[0], cropped_arr.shape[1])
    print("New shape after Transpose: ", cropped_arr.shape, "or", reshaped.shape)
    print(cropped_arr)
    # display
    plt.imshow(cropped_arr, cmap='gray')
    plt.show()


def main():
    """main
    Loads the 'animal.jpeg' and rotates it by a factor of 3.
    Image data info will be printed to terminal and image will be displayed.
    """
    try:
        image_data = ft_load("animal.jpeg")
        rotate(image_data)
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()