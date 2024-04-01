# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='froggius',
    packages=find_packages(include=['froggius']),
    description='Froggius is a dumb easy logging tool for python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MPL-2.0',
    version='0.1.3-1',
    author='zlElo',
    author_email="mail@zlelo.de",
    url = "https://github.com/zlElo/Froggius",
    keywords=['logging', 'logger', 'easy-to-use', 'log'],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows"
    ]
)
