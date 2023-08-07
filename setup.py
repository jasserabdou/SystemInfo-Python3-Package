# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='systeminfo-python3',
    version='0.1.0',
    author='Jasser Abdelfattah',
    author_email='jasserabdelfattah12@gmail.com',
    description='A package that provides system information for your device.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/jasserabdou/SystemInfo-Python3-Package',
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    packages=find_packages(),
    install_requires=['psutil', 'py-cpuinfo', 'gputil'],
    keywords=['python', 'systeminfo'],
)
