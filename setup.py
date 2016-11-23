#!/usr/bin/env python
from setuptools import setup

setup(
    name='pdfmerge3',
    version='0.1',
    description='A simple PDF merger',
    url='https://github.com/marciojmo/pdfmerge3',
    author='Marcio Oliveira',
    author_email='marciomjmo@gmail.com',
    license='MIT',
    packages=["pdfmerge3"],
    entry_points={'console_scripts':['pdfmerge3 = pdfmerge3:main']}
)
