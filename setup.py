# -*- coding: utf-8 -*-

from setuptools import setup
import io

with io.open('README.rst', 'rt', encoding='utf8') as f:
    readme = f.read()

setup(
    name="Lupyta",
    version="0.0.3",
    author="Edgardo Ortiz",
    author_email="edgardoficial.yo@gmail.com",
    description="Lupyta instalador automático de PyQt4",
    url="https://github.com/eortizromero/lupyta",
    long_description=readme,
    platforms="any",
    packages=["lupyta"],
    include_package_data=True,
    install_requires=[
        'wget'
    ]
)
