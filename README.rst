========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/spacevader/badge/?style=flat
    :target: https://readthedocs.org/projects/spacevader
    :alt: Documentation Status

.. |travis| image:: https://api.travis-ci.org/pratikms/spacevader.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/pratikms/spacevader

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/pratikms/spacevader?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/pratikms/spacevader

.. |requires| image:: https://requires.io/github/pratikms/spacevader/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/pratikms/spacevader/requirements/?branch=master

.. |codecov| image:: https://codecov.io/github/pratikms/spacevader/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/pratikms/spacevader

.. |version| image:: https://img.shields.io/pypi/v/spacevader.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/spacevader

.. |wheel| image:: https://img.shields.io/pypi/wheel/spacevader.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/spacevader

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/spacevader.svg
    :alt: Supported versions
    :target: https://pypi.org/project/spacevader

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/spacevader.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/spacevader

.. |commits-since| image:: https://img.shields.io/github/commits-since/pratikms/spacevader/v0.0.3.svg
    :alt: Commits since latest release
    :target: https://github.com/pratikms/spacevader/compare/v0.0.3...master



.. end-badges

A simple space invaders game developed purely in Python

* Free software: MIT license

.. image:: https://github.com/pratikms/spacevader/blob/master/screenshots/GameInProgress.png?raw=true "Game in progress")
.. image:: https://github.com/pratikms/spacevader/blob/master/screenshots/GameOver.png?raw=true "Game over")

Installation
============

::

    pip install spacevader

You can also install the in-development version with::

    pip install https://github.com/pratikms/spacevader/archive/master.zip


Documentation
=============


https://spacevader.readthedocs.io/


Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
