# setup.py
from setuptools import setup, find_packages

setup(
    name='NyXX',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # Add any dependencies your project needs here
    ],
    entry_points={
        'console_scripts': [
            # Optional: command-line entry points
        ],
    },
)
