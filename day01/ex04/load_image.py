import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """ft_load(path to image) -> array of rgb values

loads an image, prints its format, and its pixels
content in RGB format."""

    image = Image.open(path)
    pixel_arr = np.array(image)
    print("The shape of image is:", pixel_arr.shape)
    print(pixel_arr)
    return pixel_arr


def main():
    """main() tests for ft_load"""
    try:
        ft_load("Animal.jpeg")
    except FileNotFoundError as e:
        print(f"{type(e).__name__}: {e}")
        print("Provide the relative or absolute path for the file")
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
