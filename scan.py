import os
import shutil


class Scan():

    def __init__(self):
        self.folder_photos = r"photos"
        self.folder_printed_photos = r"printed_photos"
        self.for_print = fr"for_print"

    def scan_new_files(self):
        with os.scandir(self.folder_photos) as entries:
            new_photos = [
                entry.name for entry in entries
                if entry.is_file() and entry.name.endswith((".jpg", ".jpeg", ".png"))
            ]
        return new_photos

    def scan_png(self):
        with os.scandir(self.for_print) as entries:
            new_photos = [
                entry.name for entry in entries
                if entry.is_file() and entry.name.endswith((".png"))
            ]
        return new_photos

    def move_file(self, file, folder):

        current_file = None
        target_file = None

        if folder == "photos": #photos -> printed_photos
            current_file = os.path.join(self.folder_photos, file)
            target_file = os.path.join(self.folder_printed_photos, file)

        if folder == "for_print": #for_print -> printed_photos
            current_file = os.path.join(self.for_print, file)
            target_file = os.path.join(self.folder_printed_photos, file)

        try:
            shutil.move(current_file, target_file)
        except Exception as e:
            print(f"Error moving file: {e}")
            
