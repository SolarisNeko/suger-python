# setup.py
from setuptools import setup

PROJECT_NAME = 'suger'

PROJECT_VERSION = '0.2.2'

setup(
    name=PROJECT_NAME,
    version=PROJECT_VERSION,
    install_requires=[
        'openpyxl',
        'paramiko',
    ],
    author='SolarisNeko',
    author_email='1417015340@qq.com',
    description='simple utils'
)
