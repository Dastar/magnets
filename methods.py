from PIL import Image
from psd_tools import PSDImage


def rotate(img):
    """Rotating photos"""
    with Image.open(img) as image:
        return image.transpose(Image.ROTATE_180)


def psd_to_png(img):
    """Convert pictures from psd to png"""
    psd = PSDImage.open(img).compose()
    if psd is None:
        raise Exception("PSD has no visible pixel")

    psd.save(img.split('.')[0] + '.png')


def add_frame(frame, img):
    """Add frame to a photo"""
    # TODO: working with errors
    frame_img = Image.open(frame)
    photo = Image.open(img)
    new_framed = Image.new(frame_img.mode, frame_img.size)

    width = frame_img.size[0]
    height = int(width // 1.5)
    photo = photo.resize((width, height), Image.ANTIALIAS)

    new_framed.paste(photo, (0, 0))
    new_framed.paste(frame_img, (0, 0), frame_img)
    # TODO: decide for a normal name to tmp photo
    new_framed.save('framed.png')
