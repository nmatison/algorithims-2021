from setuptools import find_packages, setup

setup(
    name='algorithims',
packages=find_packages(include=['algorithims']),
         version='0.1.0',
description='Library for practicing algorithims, data structures, and such',
author='Nicholas Matison',
license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
tests_require=['pytest==6.2.2', 'pytest-mock==3.5.1'],
test_suite='tests',
)