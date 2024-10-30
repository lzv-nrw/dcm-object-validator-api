import os
from setuptools import setup

setup(
    version="4.1.0",
    name="dcm-object-validator-api",
    description="api for object-validator-containers",
    author="LZV.nrw",
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
