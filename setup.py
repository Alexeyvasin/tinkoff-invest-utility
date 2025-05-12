from setuptools import setup, find_packages

setup(
    name="tinkoff-invest-utility",  # Name of your library
    version="0.1",
    packages=find_packages(),  # Automatically find your packages
    install_requires=['tinkoff-investments', 'asyncio'],  # List of dependencies (if any)
    author="Alexey Vasin",
    author_email="alexeyvasin@gmail.com",
    description="Utils functions for tinkoff-invest",
    long_description="",
    long_description_content_type="text/markdown",
    url="https://github.com/Alexeyvasin/tinkoff-invest-utility",  # URL of the repo
)