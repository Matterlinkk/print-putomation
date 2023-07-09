import PIL
from PIL import Image


def place_photo(file, file_name):
    try:
        im = Image.open(file)
        a4im = Image.new("RGBA",
                         (595, 842), #A4 at 72DPI
                         (255, 255, 255, 0))
        image_width, image_height = im.size
        offset = (a4im.width - image_width, 100)
        a4im.paste(im, offset)
        a4im.save(fr"C:\Users\UA\PycharmProjects\BetterCallGoose\for_print\{file_name}", "PNG", quality=100)
        print(f"File: {file} saved")

    except FileNotFoundError:
        print(f"Error: File not found: {file}")

    except PIL.UnidentifiedImageError:
        print(f"Error: Invalid image file: {file}")

    except Exception as ex:
        print(f"An error occurred while processing the file: {ex}")

    finally:
        return fr"C:\Users\UA\PycharmProjects\BetterCallGoose\for_print\{file_name}"