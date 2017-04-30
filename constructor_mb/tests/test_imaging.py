import shutil
import tempfile

from constructor_mb.imaging import write_images


def test_write_images():
    tmp_dir = tempfile.mkdtemp()

    info = {'name': 'test', 'version': '0.3.1'}
    write_images(info, tmp_dir)

    shutil.rmtree(tmp_dir)


def test_maxiconda_images():
    tmp_dir = tempfile.mkdtemp()

    info = {'name': 'test', 'version': '0.3.1',
            'default_image_color': 'yellow',
            'welcome_image': '../../examples/maxiconda/bird.png'}
    write_images(info, '.')

    shutil.rmtree(tmp_dir)


if __name__ == '__main__':
    test_write_images()
    test_maxiconda_images()
