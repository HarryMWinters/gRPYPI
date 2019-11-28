import os

import setuptools

REQUIRED = ["google"]

cwd = os.getcwd()
with open(os.path.join(cwd, "README.md"), "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="protolib",
    version="0.0.1",
    author="Turkey M. Gobbles",
    author_email="thanksgiving_sucks@freebird.com",
    description="This package holds python code for working with protos.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HarryMWinters/gRPYPI",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=REQUIRED,
)
