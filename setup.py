#!/usr/bin/env python

from distutils.core import setup

LONG_DESCRIPTION = \
'''The program reads one or more input FASTA files.
For each file it computes a variety of statistics, and then
prints a summary of the statistics as output.

The goal is to provide a solid foundation for new bioinformatics command line tools,
and is an ideal starting place for new projects.'''


setup(
    name='fastqe-convert',
    version='0.1.0.0',
    author='FASTQE-CONVERT_AUTHOR',
    author_email='FASTQE-CONVERT_EMAIL',
    packages=['fastqe-convert'],
    package_dir={'fastqe-convert': 'fastqe-convert'},
    entry_points={
        'console_scripts': ['fastqe-convert = fastqe-convert.fastqe-convert:main']
    },
    url='https://github.com/cjwomack/fastqe-convert',
    license='LICENSE',
    description=('A prototypical bioinformatics command line tool'),
    long_description=(LONG_DESCRIPTION),
    install_requires=["fastqe","biopython>=1.66",'pyemojify'],
    
)
