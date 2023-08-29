from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in restaurant/__init__.py
from restaurant import __version__ as version

setup(
	name="restaurant",
	version=version,
	description="restaurant",
	author="Michael",
	author_email="yeungmoterial123@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
