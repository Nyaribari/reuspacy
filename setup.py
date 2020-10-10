from setuptools import setup

setup(
name='reuspacy',
version='0.0.1',
description = 'The package is a simple spacy entity ruler.',
url = 'git+ssh://git@github.com/Nyaribari/reuspacy#egg=reuspacy',
author='Nyarbari Reuben',
author_email='anyaribari@gmail.com',
licence='unlicense',
packages=['reuspacy'],
install_requires=['spacy',],
zip_safe= False
)
