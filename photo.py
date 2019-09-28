from PIL import Image
from os import path, remove
import wx


class Photo:
    EXTENSION: str = 'png'

    def __init__(self, image_path, duplicate=1):
        self.path = path.split(image_path)
        self.duplicate = duplicate
        self.framed = None

        try:
            self.photo = Image.open(image_path)
        except IOError:
            print("Failed to open file " + self.path[1])
            return

    def __call__(self, width=0):
        if self.framed is None:
            img = self.photo
        else:
            img = self.framed

        if width != 0:
            img = Photo.resize_photo(img.copy(), width)

        return img

    def undo(self):
        self.photo = Image.open(path.join(*self.path))

    def add_frame(self, frame: Image, position: tuple = (0, 0)):
        self.framed = Image.new(frame.mode, frame.size)
        self.framed.paste(self.photo, position)
        self.framed.paste(frame, (0, 0), frame)

    @staticmethod
    def resize_photo(photo: Image, width: int):
        ratio = photo.size[0] / photo.size[1]
        height = int(width / ratio)
        return photo.resize((width, height), Image.ANTIALIAS)

    def resize(self, width: int):
        self.photo = Photo.resize_photo(self.photo, width)

    def save(self):
        """Saving framed photo and duplicate it"""
        if self.duplicate != 0:
            name, extension = self.path[1].split('.')
            copy_name = name + '%s.' + self.EXTENSION

            if self.framed is None:
                print("No framed photo found")
                return

            for i in range(self.duplicate):
                self.framed.save(
                    path.join(self.path[0],
                              copy_name % ('_copy_' + str(i))),
                    self.EXTENSION)

        remove(path.join(self.path[0], self.path[1]))

    def light(self, ration):
        self.photo = self.photo.point(lambda p: p * ration)

    @staticmethod
    def bitmap_from_pil_image(caller, pil_image):
        wx_image = wx.Image(pil_image.size[0], pil_image.size[1])
        wx_image.SetData(pil_image.convert("RGB").tobytes())
        bitmap = wx.Bitmap(wx_image)
        return bitmap
