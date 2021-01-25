from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='Scrapper for Social Media ',
    version='1.2.0',

    description='T',
    long_description = long_description,

 

     classifiers = [

                       'Development Status :: 4 - Beta',

                       'Programming Language :: Python :: 3',
                       'Programming Language :: Python :: 3.3',
                       'Programming Language :: Python :: 3.4',
                       'Programming Language :: Python :: 3.5',
                       'Programming Language :: Python :: 3.6',
                   ],

     keywords = 'python twitter tweepy instagram scrapper crawler hashtags hashtag images image caption',

    install_requires = ['tweepy',
                        'openpyxl',
                        'selenium'],


)
