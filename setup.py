import sys, requests
from setuptools import setup

setup(
    name="s1db",
    version="1.0.0",
    author="Max Bridgland",
    author_email="mabridgland@protonmail.com",
    description="S1 API Library for Python",
    long_description=open('./README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/M4cs/s1db-python",
    packages=['s1db'],
    install_requires=['requests'],
    tests_require=['unittest'],
    zip_safe=True,
    project_urls={
        'S1': 'https://github.com/kognise/s1',
        's1db-node': 'https://github.com/kognise/s1-node'
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',

        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: IronPython',
        'Programming Language :: Python :: Implementation :: Jython',

        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Information Technology',

        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries',
        'Topic :: System :: Systems Administration',
        'Topic :: System :: Networking',
        'Topic :: Utilities',
    ]
)