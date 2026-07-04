from setuptools import setup, find_packages

setup(
    name="insights_framework",
    version="1.0.0",
    packages=find_packages(),
    install_requires=["pytest"],
    description="Shared ML pipeline base class for all BU audience models",
)
