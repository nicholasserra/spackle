#!/usr/bin/env python

from setuptools import setup

setup(
    name='spackle',
    version='0.0.2',
    install_requires=['setuptools', 'coverage'],
    author='Nicholas Serra',
    author_email='nickserra@gmail.com',
    license='MIT License',
    url='https://github.com/nicholasserra/spackle/',
    keywords=['spackle', 'coverage', 'testing'],
    description='Help identify gaps in python code coverage.',
    long_description=open('README.md').read(),
    download_url="https://github.com/nicholasserra/spackle/zipball/master",
    packages=['spackle'],
    entry_points={
        'console_scripts': [
            'spackle = spackle.script:main',
    ]},
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet'
    ]
)
