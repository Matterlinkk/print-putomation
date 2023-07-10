import os
import time


scanner = Scan()


while True:

    value = scanner.scan_new_files()
    png = scanner.scan_png()

    if value:
        print(f"New file: {value[0]}")
        place_photo(os.path.join(scanner.folder_photos, value[0]), f"{value[0].split('.')[0]}.png")
        scanner.move_file(value[0], folder="photos")

    if png:
        print_file(os.path.join(scanner.for_print, png[0]))
        scanner.move_file(png[0], folder="for_print")

    time.sleep(15)
