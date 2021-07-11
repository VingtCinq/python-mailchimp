#!/usr/bin/env python
import os
from setuptools import setup, find_packages


README = os.path.join(os.path.dirname(__file__), 'README.rst')

# When running tests using tox, README.md is not found
try:
    with open(README) as file:
        long_description = file.read()
except Exception:
    long_description = ''


setup(
    name='mailchimp3',
    version='3.0.15',
    description='A python client for v3 of MailChimp API',
    long_description=long_description,
    url='https://github.com/charlesthk/python-mailchimp',
    author='Charles TISSIER',
    author_email='charles@vingtcinq.io',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='mailchimp api v3 client wrapper',
    packages=find_packages(),
    install_requires=['requests>=2.7.0'],
    # test_suite='tests',
)
