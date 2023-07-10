import PIL
from PIL import Image

#select the desired option(CENTER OR RIGHT)
FOR_CENTERED_PICTURES = (529, 297)
FOR_RIGHT_SIDE_PICTURE = (345, 194)


def place_photo(file, file_name):
    try:
        im = Image.open(file)
        im = im.resize(FOR_RIGHT_SIDE_PICTURE)
        im = im.convert("L")
        a4im = Image.new("RGBA",
                         (595, 842), #A4 at 72DPI
                         (255, 255, 255, 0))
        image_width, image_height = im.size
        # Two identical options must be selected (CENTER OR RIGHT)

        CENTERED_IMAGE = (a4im.width - image_width) // 2, 110
        RIGHT_SIDE_IMAGE = ((a4im.width - image_width) // 2 + 90, 103)

        offset = (RIGHT_SIDE_IMAGE)
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
