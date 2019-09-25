from PIL import Image
from os import path


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

    def __call__(self):
        if self.framed is None:
            return self.photo
        else:
            return self.framed

    def add_frame(self, frame: Image, position: tuple = (0, 0)):
        self.framed = Image.new(frame.mode, frame.size)
        self.framed.paste(self.photo, position)
        self.framed.paste(frame, (0, 0), frame)

    def resize(self, width: int):
        ratio = self.photo.size[0] / self.photo.size[1]
        height = int(width / ratio)
        self.photo = self.photo.resize((width, height), Image.ANTIALIAS)

    def save(self):
        """Saving framed photo and duplicate it"""
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

    def light(self, ration):
        self.photo = self.photo.point(lambda p: p * ration)
