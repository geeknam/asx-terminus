from setuptools import find_packages
from setuptools import setup


requires = [
    "requests>=2.18.4",
    "urwid>=1.3.1",
    "pyyaml>=3.12",
    "beautifulsoup4==4.6.0",
]

setup(
    name='asx-terminus',
    packages=find_packages(
        exclude=['tests',]
    ),
    license='Apache 2.0',
    version='0.1.3',
    description='ASX portfolio in the terminal',
    long_description=open('README.md').read(),
    author='Nam Ngo',
    author_email='namngology@gmail.com',
    keywords=[
        'asx', 'terminal', 'urwid', 'ncurses',
        'australia', 'investment', 'stock'
    ],
    install_requires=requires,
    entry_points={
        'console_scripts': [
            'asxterminus = asxterminus.cli:main'
        ]
    },
)