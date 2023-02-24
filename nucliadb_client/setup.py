# -*- coding: utf-8 -*-
import re

from setuptools import find_packages, setup

VERSION = open("../VERSION").read().strip()
README = open("README.md").read()


def load_reqs(filename):
    with open(filename) as reqs_file:
        return [
            # pin nucliadb-xxx to the same version as nucliadb
            line.strip() + f"=={VERSION}"
            if line.startswith("nucliadb-") and "=" not in line
            else line.strip()
            for line in reqs_file.readlines()
            if not (
                re.match(r"\s*#", line) or re.match("-e", line) or re.match("-r", line)
            )
        ]


requirements = load_reqs("requirements.txt")

setup(
    name="nucliadb_client",
    version=VERSION,
    long_description=README,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
    ],
    url="https://nuclia.com",
    license="BSD",
    zip_safe=True,
    include_package_data=True,
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "nucliadb_export = nucliadb_client.export:run",
            "nucliadb_import = nucliadb_client.importing:run",
        ]
    },
)
