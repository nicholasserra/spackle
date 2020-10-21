#!/usr/bin/env python

from setuptools import setup

setup(
    name='spackle',
    version='0.0.3',
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
    python_requires=">=2.7, <4",
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ]
)
