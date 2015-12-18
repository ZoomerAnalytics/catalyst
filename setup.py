import os
import re
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'catalyst', '__init__.py')) as f:
    version = re.compile(r".*__version__ = '(.*?)'", re.S).match(f.read()).group(1)

setup(
    name='catalyst',
    packages=find_packages(),
    version=version,
    description='Simple database migration for SQLAlchemy',
    author='Zoomer Analytics LLC',
    author_email='eric.reynolds@zoomeranalytics.com',
    url='https://github.com/ZoomerAnalytics/catalyst',
    keywords=['sql', 'database', 'migration', 'sqlalchemy'],
    install_requires=[
        'six',
        'iso8601'
    ],
    entry_points={
        'console_scripts': [
            'catalyst=catalyst.cli:main'
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
)
