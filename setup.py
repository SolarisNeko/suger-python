# setup.py
from setuptools import setup

PROJECT_NAME = 'suger'

PROJECT_VERSION = '0.1.0'

setup(
    name=PROJECT_NAME,
    version=PROJECT_VERSION,
    install_requires=[
        'paramiko',
        'openpyxl'
    ],
    author='SolarisNeko',
    author_email='1417015340@qq.com',
    description='simple utils'
)
