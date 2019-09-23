from PIL import Image


class Photo:
    def __init__(self, image_path):
        self.path = image_path
        try:
            self.photo = Image.open(image_path)
        except IOError:
            print("Failed to open file " + image_path)
            return

    def add_frame(self, frame):
        pass
