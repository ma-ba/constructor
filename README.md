constructor-mb
==============

This is a fork of [constructor] with some features added which currently
aren't included in `constructor` itself.
This fork is mainly meant for my own personal use, thus I strongly suggest to
use the original package.
All (or at least most) changes will be issued as pull request to `constructor`.
If you feel the need to use any of those, leave a comment on the corresponding
PR at the [constructor pull requests site].

[constructor]: https://github.com/conda/constructor
[constructor pull requests site]: https://github.com/conda/constructor/pulls


Changes in constructor-mb:
--------------------------

  * Add optional readme.txt support [constructor/#66]
  * Add customization for welcome and header image texts [constructor/#67]
  * Add ability to provide defaults for custom options [constructor/#68]
  * Add basic jinja2 support [constructor/#74]
  * Remove menus of all conda envs during uninstall [constructor/#75]
  * Use setuptools package\_data/entry\_points, enable egg/wheel builds
    [constructor/#76]

[constructor/#66]: https://github.com/conda/constructor/pull/66
[constructor/#67]: https://github.com/conda/constructor/pull/67
[constructor/#68]: https://github.com/conda/constructor/pull/68
[constructor/#74]: https://github.com/conda/constructor/pull/74
[constructor/#75]: https://github.com/conda/constructor/pull/75
[constructor/#76]: https://github.com/conda/constructor/pull/76


(conda) constructor
===================

constructor is a tool which allows constructing an installer for
a collection of conda packages.  Basically, it creates an Anaconda-like
installer consisting of conda packages.   This tool was previously
proprietary and known as `cas-installer`.


Installation:
-------------

As of version 1.3.0, `constructor` may be installed into any conda
environment using:

    $ conda install constructor

Once installed, the constructor command will be available:

    $ constructor -h


Usage:
------

The `constructor` command takes an installer specification directory as its
argument.  This directory needs to contain a file `construct.yaml`,
which specifies the name of the installer, the conda channels to
pull packages from, the conda packages included in the installer etc. .
The complete list of keys in this file can be
found in <a href="./CONSTRUCT.md">CONSTRUCT.md</a>.
Also, the directory may contain some additional optional files (such as a
license file, and image files for the Windows installer).
An example is located
in <a href="./examples/maxiconda">examples/maxiconda</a>.


Notes:
------

  * Constructor does not work with `noarch`-Python packages.
    All conda packages must be available for the platform you are
    building the installer for.
  * An installer created by constructor does not need to include `conda`
    itself.  If you require the ability to use `conda` after installation,
    add `conda` to the package list.
  * An installer created by constructor is not the same as Miniconda.  All
    packages you want to include in the installer need to be listed
    explicitly.
    In particular, on Windows this means that if you want the "Anaconda
    Prompt", you will have to list `console_shortcut`, as well as `menuinst`.
  * For Windows builds, add the Continuum channels `/free` and `/msys2`
    to the file `constructor.yaml`. This provides packages such as
    `m2w64-toolchain` which is a dependency of `theano`. It is best to
    add `/msys2` as `http://repo.continuum.io/pkgs/msys2`.
