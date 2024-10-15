"""
 * devs free ( developers free ) OSS
 * author: github.com/alisharify7
 * email: alisharifyofficial@gmail.com
 * license: see LICENSE for more details.
 * Copyright (c) 2023 - ali sharifi
 * https://github.com/alisharify7/devs_free
"""


from setuptools import setup, find_packages

__NAME__ = "devs_free"
__version__ = "1.0.1"
__author__ = "ali sharify"
__author_mail__ = "alisharifyofficial@gmail.com"
__copyright__ = "ali sharify - 2024"
__license__ = "GPL-3.0 license"
__short_description__ = "devs-free is a CLI tool to help you develop easily and freely."


with open("./README.md", "r") as f:
    long_description = f.read()
    setup(
        name=__NAME__,
        version=__version__,
        description=__short_description__,
        packages=find_packages(),
        author_email=__author_mail__,
        author=__author__,
        url="https://github.com/alisharify7/devs-free",
        long_description=long_description,
        long_description_content_type="text/markdown",
        classifiers=[
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
            "Programming Language :: Python :: 3.12",
            "Environment :: CLI",
            "Topic :: Security",
        ],
        license=__license__,
        install_requires=[
            "requests>=2.30.0",
            # "simple_term_menu>=1.6.4",
            "pyfiglet>=1.0.2",
            # "inquirerpy>=0.3.4",
            "questionary>=2.0.1",
            "click>=8.1.7"
        ],
        python_requires=">=3.8",
        keywords='dns, cli, python-dns-changer',
        entry_points={
            'console_scripts': [
                'devs_free = devs_free.cli_entrypoint:devs',
                'devs-free = devs_free.cli_entrypoint:devs',
                'developer-free = devs_free.cli_entrypoint:devs',
                'developer_free = devs_free.cli_entrypoint:devs',
            ],
        },

    )

