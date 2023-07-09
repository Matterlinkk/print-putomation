from scan import Scan
from pillow import place_photo
from printer import Printer
import os
import time


scanner = Scan()
printer = Printer()

while True:

    value = scanner.scan_new_files()

    if value:
        print(f"New file: {value[0]}")
        printer.print_file(place_photo(os.path.join(scanner.folder_photos, value[0]), f"{value[0].split('.')[0]}.png"))
        scanner.move_file(value[0])

    time.sleep(20)

