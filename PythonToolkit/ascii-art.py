"""
How it works?

We scale a given image to a standard resolution that suitably represents the ASCII version of a given image. The scaled version is then converted to a grayscale image. In a grayscale image, there are 256 shades of gray, or in other words, each pixel carries only the intensity information which is represented by an 8 bit value. A pixel with a value of 0 is assumed to be black and the one with 255 is assumed to be white. We divide the whole range of 0-255 into 11 smaller ranges of 25 pixels each and then assign each pixel a character according to the range it falls in. The point is to assign a group of pixels with slightly varying intensity the same ASCII char. We use the PIL library to play with the images. The code given below is almost self explanatory. The default char mapping and resolution doesn't render good ASCII arts for every image size and so you should try modifying the char mapping and image size to the one that best represents the given image.

From: http://www.hackerearth.com/notes/beautiful-python-a-simple-ascii-art-generator-from-images/

Dependencies:

PIL(Python Imaging Library)

"""

from PIL import Image

ASCII_CHARS = [ '#', '?', '%', '.', 'S', '+', '.', '*', ':', ',', '@']

def scale_image(image, new_width=100):
    """Resizes an image preserving the aspect ratio.
    """
    (original_width, original_height) = image.size
    aspect_ratio = original_height/float(original_width)
    new_height = int(aspect_ratio * new_width)

    new_image = image.resize((new_width, new_height))
    return new_image

def convert_to_grayscale(image):
    return image.convert('L')

def map_pixels_to_ascii_chars(image, range_width=25):
    """Maps each pixel to an ascii char based on the range
    in which it lies.

    0-255 is divided into 11 ranges of 25 pixels each.
    """

    pixels_in_image = list(image.getdata())
    pixels_to_chars = [ASCII_CHARS[pixel_value//range_width] for pixel_value in
            pixels_in_image]

    return "".join(pixels_to_chars)

def convert_image_to_ascii(image, new_width=100):
    image = scale_image(image)
    image = convert_to_grayscale(image)

    pixels_to_chars = map_pixels_to_ascii_chars(image)
    len_pixels_to_chars = len(pixels_to_chars)

    image_ascii = [pixels_to_chars[index: index + new_width] for index in
            range(0, len_pixels_to_chars, new_width)]

    return "\n".join(image_ascii)

def handle_image_conversion(image_filepath):
    image = None
    try:
        image = Image.open(image_filepath)
    except Exception as e:
        print("Unable to open image file {image_filepath}.".format(image_filepath=image_filepath))
        print(e)
        return

    image_ascii = convert_image_to_ascii(image)
    print(image_ascii)

if __name__=='__main__':
    import sys
    image_file_path = sys.argv[1]
    handle_image_conversion(image_file_path)
