from setuptools import setup, find_packages
from typing import List



# read requirements.txt
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="my_project",
    version="0.1",
    author="Amursetti Pavani",
    author_email="pavaniroyal66@gmail.com",
    packages=find_packages(),
    install_requires=requirements
)