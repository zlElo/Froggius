from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='froggius',
    packages=find_packages(include=['froggius']),
    description='Froggius is a dumb easy logging tool for python',
    long_description=long_description,
    version='0.1.3',
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
