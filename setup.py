# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "clashofcubicles"
VERSION = "0.0.1"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["connexion"]

setup(
    name=NAME,
    version=VERSION,
    description="Clash of Cubicles",
    author_email="greg@luzene.com",
    url="",
    keywords=["Swagger", "Clash of Cubicles"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    long_description="""\
    Clash of Cubicles is multiplayer RPG which simulates the Kafka-esque aspects of the cubicle rat-race, and the growth and reward of advancing up the hamster wheel faster than your peers.
    """
)

