"""setup"""
import os
import codecs
from setuptools import setup
from cleantext import __maintainer__, __version__

rootdir = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(rootdir, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

setup(
    name='cleantext',
    version=__version__,
    description='An open-source python package to clean raw text data',
    author=__maintainer__,
    author_email='prasanth.gudiwada@gmail.com',
    url='https://github.com/prasanthg3/cleantext',
    license='MIT',
    long_description="\n" + fh.read(),
    long_description_content_type='text/markdown',
    packages=['cleantext'],
    install_requires=['nltk'],
)
