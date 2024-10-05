from setuptools import setup
from setuptools import find_packages

setup(
    name="healthkg",
    version="0.0.1",
    description="healthcare knowledge-graph  CLI",
    keywords="healthcare-kg",
    author="",
    author_email="",
    url="",
    install_requires=[
        "python-arango",
        "basescript==0.3.9",
        "pandas==1.3.5"
    ],
    package_dir={"healthkg": "healthkg"},
    packages=find_packages("."),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Environment :: Console",
        "Intended Audience :: Developers",
    ],
    entry_points={"console_scripts": ["healthkg = healthkg:main"]},
)
