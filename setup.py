import os
from setuptools import setup
from cleantext import __maintainer__,__version__


rootdir = os.path.abspath(os.path.dirname(__file__))
setup(
   name='cleantext',
   version=__version__,
   description='An open-source python package to clean raw text data',
   
   author=__maintainer__,
   author_email='prasanth.gudiwada@gmail.com',
   url='https://github.com/prasanthg3/cleantext',
   license='MIT',
   long_description = open(os.path.join(rootdir, 'README.md')).read(),
   long_description_content_type='text/markdown',
   packages=['cleantext'],  
   install_requires=['nltk'],
)