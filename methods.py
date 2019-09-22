from PIL import Image
from glob import glob
import os


# TODO: working with errors
def rotate(img):
    """Rotating photos"""
    with Image.open(img) as image:
        return image.transpose(Image.ROTATE_180)


def psd_to_png(img):
    """Convert pictures from psd to png"""
    from psd_tools import PSDImage
    psd = PSDImage.open(img).compose()
    if psd is None:
        raise Exception("PSD has no visible pixel")

    psd.save(img.split('.')[0] + '.png')


def add_frame(frame, img):
    """Add frame to a photo"""
    frame_img = Image.open(frame)
    photo = Image.open(img)
    new_framed = Image.new(frame_img.mode, frame_img.size)

    width = frame_img.size[0]
    height = int(width // (photo.size[0] / photo.size[1]))
    photo = photo.resize((width, height), Image.ANTIALIAS)

    new_framed.paste(photo, (0, 0))
    new_framed.paste(frame_img, (0, 0), frame_img)

    new_framed.save(img.split('.')[0] + '.png')
    os.remove(img)


def create_print(photos, name):
    """Creating a picture with four framed images"""
    final_photo = Image.new('RGB', (2400, 1800))
    positions = [(0, 0), (0, 900), (1200, 0), (1200, 900)]
    i = 0

    for img in photos:
        photo = Image.open(img)
        final_photo.paste(photo, positions[i])
        i += 1

        os.remove(img)

    final_photo.save(name)


def run_over_all_photos(path, frame, save_folder, start_name_from=0):
    """Run through all photos in path, frames them and put them into list of four"""
    all_photos = glob(os.path.join(path, "*.JPG"))
    all_photos += glob(os.path.join(path, "*.jpg"))
    for photo in all_photos:
        add_frame(frame, photo)

    all_photos = [x.split('.')[0] + '.png' for x in all_photos]
    all_photos = [all_photos[x, x + 4] for x in range(0, len(all_photos), 4)]
    for photos in all_photos:
        create_print(photos, os.path.join(save_folder, str(start_name_from) + '.png'))
        start_name_from += 1
