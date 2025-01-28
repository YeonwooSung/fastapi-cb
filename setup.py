#!/usr/bin/env python
# -*- coding:utf-8 -*-

from setuptools import setup, find_packages

from fastapi_cb import version


with open("readme.md", "r") as fh:
    long_description = fh.read()


test_dependencies = [
    'fakeredis', 'pytest>4', 'pytest-asyncio',
    'mypy', 'pylint', 'safety', 'bandit', 'codecov', 'pytest-cov'
]
redis_dependencies = ['redis']
documentation_dependencies = [
    'sphinx', 'sphinx_rtd_theme', 'sphinx-autobuild', 'sphinx-autodoc-typehints'
]


setup(
    name='fastapi_cb',
    version=version.__version__,
    url='https://github.com/YeonwooSung/fastapi-cb',
    license='BSD',
    author='Yeonwoo Sung',
    author_email='neos960518@gmail.com',
    description='Circuit Breaker implementation for FastAPI.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    py_modules=['asyncbreaker'],
    python_requires='>=3.8',
    install_requires=[],
    tests_require=test_dependencies,
    extras_require={
        'test': test_dependencies,
        'docs': documentation_dependencies,
        'redis': redis_dependencies,
    },
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Libraries',
    ],
)
