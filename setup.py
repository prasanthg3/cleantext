from setuptools import setup

with open("README", 'r') as f:
    long_description = f.read()

setup(
   name='cleantext',
   version='1.0.0',
   description='A package to clean the raw text',
   author='Prasanth Gudiwada',
   author_email='prasanth.gudiwada@gmail.com',
   license='MIT',
   packages=['cleantext'],  
   install_requires=['nltk', 're', 'string'],
)