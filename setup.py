import os
from setuptools import setup

setup(
    version="5.1.0",
    name="dcm-object-validator-api",
    description="specification of the DCM Object Validator API",
    author="LZV.nrw",
    license="MIT",
    install_requires=[
    ],
    packages=[
        "dcm_object_validator_api",
    ],
    package_data={
        "dcm_object_validator_api": [
            "dcm_object_validator_api/openapi.yaml",
        ],
    },
    include_package_data=True,
)
