from setuptools import find_packages, setup

setup(
    name="dagsterflightpricerepo",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "dagster",
        "dagster-cloud",
        "dagster-databricks",
        "dagster-aws",
        "pyspark",
        "boto3",
        "requests",
    ],
)
