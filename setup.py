from setuptools import find_packages, setup

setup(
    name='froggius',
    packages=find_packages(include=['froggius']),
    description='Froggius is a dumb easy logging tool for python',
    version='{{VERSION_PLACEHOLDER}}',
    author='zlElo',
    author_email="mail@zlelo.de",
    url = "https://github.com/zlElo/Froggius",
    keywords=['pypi', 'cicd', 'python'],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows"
    ]
)
