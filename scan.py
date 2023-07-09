import os
import shutil


class Scan():

    def __init__(self):
        self.folder_photos = r"C:\Users\UA\PycharmProjects\BetterCallGoose\photos"
        self.folder_printed_photos = r"C:\Users\UA\PycharmProjects\BetterCallGoose\printed_photos"

    def scan_new_files(self):
        with os.scandir(self.folder_photos) as entries:
            new_photos = [
                entry.name for entry in entries
                if entry.is_file() and entry.name.endswith((".jpg", ".jpeg", ".png"))
            ]
        return new_photos

    def move_file(self, file):
        current_file = os.path.join(self.folder_photos, file)
        target_file = os.path.join(self.folder_printed_photos, file)

        try:
            shutil.move(current_file, target_file)
        except Exception as e:
            print(f"Error moving file: {e}")
