"""setup"""
import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (HERE / 'README.md').read_text(encoding='utf-8')
__version__ = '1.1.4'
__maintainer__ = 'Prasanth Gudiwada'

setup(
    name='cleantext',
    version=__version__,
    description='An open-source python package to clean raw text data',
    author=__maintainer__,
    author_email='prasanth.gudiwada@gmail.com',
    url='https://github.com/prasanthg3/cleantext',
    license='MIT',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=['cleantext'],
    install_requires=['nltk'],
    tests_require=['pytest']
)
