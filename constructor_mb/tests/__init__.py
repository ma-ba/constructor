# (c) 2017 Marcel Bargull
# (c) 2016 Continuum Analytics, Inc. / http://continuum.io
# All Rights Reserved
#
# constructor-mb is distributed under the terms of the BSD 3-clause license.
# Consult LICENSE.txt or http://opensource.org/licenses/BSD-3-Clause.

from __future__ import print_function, division, absolute_import

import sys

import libconda

import constructor_mb
from constructor_mb.tests import test_parser, test_utils, test_install


def main():
    print("sys.prefix: %s" % sys.prefix)
    print("sys.version: %s ..." % (sys.version[:40],))
    print('constructor-mb version:', constructor_mb.__version__)
    print('libconda version:', libconda.__version__)
    print('location:', constructor_mb.__file__)

    if sys.platform == 'win32':
        import PIL
        from constructor_mb import winexe
        from constructor_mb.tests.test_imaging import test_write_images

        print('pillow version: %s' % PIL.PILLOW_VERSION)
        winexe.verify_nsis_install()
        winexe.read_nsi_tmpl()
        test_write_images()
    else:
        from constructor_mb import shar
        shar.read_header_template()

    test_parser.test_1()
    test_utils.main()
    assert test_install.run().wasSuccessful() == True


if __name__ == '__main__':
    main()
