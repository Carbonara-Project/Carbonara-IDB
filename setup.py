#!/usr/bin/env python
from setuptools import setup, find_packages

# For Testing:
#
# python3.4 setup.py register -r https://testpypi.python.org/pypi
# python3.4 setup.py bdist_wheel upload -r https://testpypi.python.org/pypi
# python3.4 -m pip install -i https://testpypi.python.org/pypi
#
# For Realz:
#
# python3.4 setup.py register
# python3.4 setup.py bdist_wheel upload
# python3.4 -m pip install

setup(
    name='carbonara-idb',
    version='0.4.0',
    description='Pure Python parser for IDA Pro databases (.idb files). Fork used in Guanciale.',
    author='Willi Ballenthin',
    author_email='willi.ballenthin@gmail.com',
    maintainer="Andrea Fioraldi",
    maintainer_email="andreafioraldi@gmail.com",
    url='https://github.com/Carbonara-Project/Carbonara-IDB',
    license='Apache License 2.0',
    install_requires=[
        'six',
        'hexdump',
        'vivisect-vstruct-wb>=1.0.3',
    ],
    packages=find_packages(exclude=['*.tests', '*.tests.*']),
    entry_points={
        "console_scripts": [
        ]
      },

    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
    ],
)
