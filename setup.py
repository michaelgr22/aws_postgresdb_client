from setuptools import setup

VERSION = '0.0.3.1'
DESCRIPTION = 'postgresdb client for aws python image'
LONG_DESCRIPTION = 'postgresdb client for aws python image'

# Setting up
setup(
    name="aws_postgresdb_client",
    version=VERSION,
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=['aws_postgresdb_client'],
    install_requires=['aws-psycopg2'],
)
