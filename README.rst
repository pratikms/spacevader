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
.. |docs| image:: https://readthedocs.org/projects/spacevaders/badge/?style=flat
    :target: https://readthedocs.org/projects/spacevaders
    :alt: Documentation Status

.. |travis| image:: https://api.travis-ci.org/pratikms/spacevaders.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/pratikms/spacevaders

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/pratikms/spacevaders?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/pratikms/spacevaders

.. |requires| image:: https://requires.io/github/pratikms/spacevaders/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/pratikms/spacevaders/requirements/?branch=master

.. |codecov| image:: https://codecov.io/github/pratikms/spacevaders/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/pratikms/spacevaders

.. |version| image:: https://img.shields.io/pypi/v/spacevaders.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/spacevaders

.. |wheel| image:: https://img.shields.io/pypi/wheel/spacevaders.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/spacevaders

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/spacevaders.svg
    :alt: Supported versions
    :target: https://pypi.org/project/spacevaders

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/spacevaders.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/spacevaders

.. |commits-since| image:: https://img.shields.io/github/commits-since/pratikms/spacevaders/v0.0.1.svg
    :alt: Commits since latest release
    :target: https://github.com/pratikms/spacevaders/compare/v0.0.1...master



.. end-badges

A simple space invaders game developed purely in Python

* Free software: MIT license

Installation
============

::

    pip install spacevaders

You can also install the in-development version with::

    pip install https://github.com/pratikms/spacevaders/archive/master.zip


Documentation
=============


https://spacevaders.readthedocs.io/


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
