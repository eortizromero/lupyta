# -*- coding: utf-8 -*-

from setuptools import setup


setup(
    name="Lupyta",
    version="1.0",
    author="Edgardo Ortiz",
    author_email="edgardoficial.yo@gmail.com",
    description="Lupyta instalador automático de PyQt4",
    long_description="Lupyta es un instalador automático de PyQt4 para los sistemas "
                "Operativos Windows® y GNU/Linux (GNU General Public License)",
    platforms="any",
    packages=["lupyta"],
    include_package_data=True,
    install_requires=[
        'wget'
    ]
)
