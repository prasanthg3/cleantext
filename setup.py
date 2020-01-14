import os
from setuptools import setup


rootdir = os.path.abspath(os.path.dirname(__file__))
setup(
   name='cleantext',
   version='1.1.3',
   description='An open-source python package to clean raw text data',
   
   author='Prasanth Gudiwada',
   author_email='prasanth.gudiwada@gmail.com',
   url='https://github.com/prasanthg3/cleantext',
   license='MIT',
   long_description = open(os.path.join(rootdir, 'README.md')).read(),
   long_description_content_type='text/markdown',
   packages=['cleantext'],  
   install_requires=['nltk'],
)