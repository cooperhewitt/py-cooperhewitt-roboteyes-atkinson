#!/usr/bin/env python

from setuptools import setup, find_packages

packages = find_packages()
desc = open("README.md").read(),

setup(
    name='cooperhewitt.roboteyes.atkinson',
    namespace_packages=['cooperhewitt'],
    version='0.2',
    description='',
    author='Cooper Hewitt Smithsonian Design Museum',
    url='https://github.com/cooperhewitt/py-cooperhewitt-roboteyes-atkinson',
    dependency_links=[
        'https://github.com/migurski/atkinson/tarball/master#egg=atk-0.1',
      ],
    install_requires=[
        'atk',
    ],
    packages=packages,
    scripts=[],
    download_url='https://github.com/cooperhewitt/py-cooperhewitt-roboteyes-atkinson/releases/tag/v0.2',
    license='BSD')
