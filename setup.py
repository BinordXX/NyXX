from setuptools import setup, find_packages

setup(
    name='NyXX',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'numpy',           # Example external dependencies
        'pandas',          # Add any required dependencies here
        'scikit-learn',
    ],
    extras_require={
        'dev': ['pytest', 'black'],  # Development dependencies
    },
    entry_points={
        'console_scripts': [
            'nyxx-simulation = scripts.run_simulations:main',  # Make sure this matches your script
        ],
    },
)
