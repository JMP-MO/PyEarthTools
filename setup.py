import os
from pathlib import Path

from setuptools import find_packages, setup

this_directory = Path(__file__).parent
install_requires = (this_directory / "requirements.txt").read_text().splitlines()
long_description = (this_directory / "README.md").read_text()

setup(
    name="FourCastNext",
    version="1.0",
    packages=["fourcastnext"],
    url="",
    description="FourCastNext Model for EDIT",
    install_requires=install_requires,
    long_description=long_description,
    long_description_content_type="text/markdown",

)
