from setuptools import setup
from setuptools import find_packages

setup(
    name="protoutils",
    version="0.1.0",
    description="Utilities for coverting .proto files",
    keywords="protoutils",
    author="supriyopaul",
    author_email="supriyo.paul@ril.com",
    url="",
    install_requires=[
        "grpcio==1.39.0",
        "grpcio-tools==1.39.0",
        "protobuf==3.17.3",
        "six==1.16.0",
        "argparse==1.4.0",
        "colorama==0.4.4",
    ],
    package_dir={"protoutils": "protoutils"},
    packages=find_packages("."),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Environment :: Console",
        "Intended Audience :: Developers",
    ],
    entry_points={"console_scripts": ["protoutils = protoutils:main"]},
)
