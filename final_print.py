from PIL import Image
from glob import glob
from itertools import cycle
from os import remove, path


class FinalPrint:
    EXTENSION: str = 'png'
    MODE: str = 'RGB'

    def __init__(self, frame: str, photos_folder: str, print_folder: str):
        self.photos_folder = photos_folder
        self.print_folder = print_folder

        try:
            self.frame = Image.open(frame)
        except IOError:
            print("ERROR: Cannot open the frame, terminating program")
            exit()

        # getting the last file name in print folder
        all_prints = glob(path.join(print_folder, '*.' + self.EXTENSION))
        if all_prints and False:
            all_prints = [int(x.split('.')[0]) for x in all_prints]
            all_prints.sort()

            self.print_name = all_prints[-1]
        else:
            self.print_name = 1

    def __call__(self):
        return self.frame

    def create_print(self, row=2, column=2, print_size=(2400, 1800)):
        """Creating pictures to print out of all framed pictures"""

        def one_page():
            final_photo = Image.new(self.MODE, print_size)
            row_step = int(print_size[0] / row)
            column_step = int(print_size[1] / column)

            for i in range(0, print_size[0], row_step):
                for j in range(0, print_size[1], column_step):
                    try:
                        img = next(photos)
                        photo = Image.open(img)
                    except IOError:
                        print("ERROR: cannot create a printable photo")
                        return

                    final_photo.paste(photo, (i, j))
                    remove(img)

            return final_photo

        photo_per_page = row * column

        # dividing all pictures to groups of photo_per_page
        all_photo = glob(path.join(self.photos_folder, '*.' + self.EXTENSION))
        all_photo = [all_photo[x:x + photo_per_page]
                     for x in range(0, len(all_photo), photo_per_page)]

        # creating printable page
        for photos in all_photo:
            if len(photos) < photo_per_page:
                break

            photos = cycle(photos)
            to_print = one_page()

            self.print_name += 1
            self.printer(to_print)
            to_print.save(path.join(self.print_folder,
                                    str(self.print_name) + "." + self.EXTENSION))

    def printer(self, photo):
        """Method that sends to the printer photos"""
        # TODO
        pass
