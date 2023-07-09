import win32print
import win32ui
from PIL import Image, ImageWin


class Printer():

    def __init__(self):
        self.printer = self.__get_printer_names()[0]

    def print_file(self, file_path):
        PHYSICALWIDTH = 110
        PHYSICALHEIGHT = 111

        hDC = win32ui.CreateDC()
        hDC.CreatePrinterDC(self.printer)
        printer_size = hDC.GetDeviceCaps(PHYSICALWIDTH), hDC.GetDeviceCaps(PHYSICALHEIGHT)

        bmp = Image.open(file_path)
        if bmp.size[0] < bmp.size[1]:
            bmp = bmp.rotate(90)

        hDC.StartDoc(file_path)
        hDC.StartPage()

        dib = ImageWin.Dib(bmp)
        dib.draw(hDC.GetHandleOutput(), (0, 0, printer_size[0], printer_size[1]))

        hDC.EndPage()
        hDC.EndDoc()
        hDC.DeleteDC()

    def __get_printer_names(self):
        printer_names = []
        printers = win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL | win32print.PRINTER_ENUM_CONNECTIONS)
        for printer in printers:
            printer_name = printer[2]
            printer_names.append(printer_name)
        return printer_names
