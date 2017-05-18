from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='complaint-search',
    version='1.0.0',

    description='Experimenting building python modules that query elasticsearch',
    long_description=long_description,
    url='https://github.com/amymok/complaint-search',
    author='CFPB',
    author_email='tech@cfpb.gov',
    license='CC0',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='query elasticsearch module',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['elasticsearch>=2,<5', 'requests', 'urllib3'],
)