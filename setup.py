from setuptools import setup

__version__ = '0.1'
__author__ = 'jpellerin@gmail.com'

setup(
    name='noseGAE',
    version=__version__,
    author=__author__,
    entry_points = {
        'nose.plugins.0.10': [ 'nosegae = nosegae:NoseGAE']
        },
    py_modules = ['nosegae'],
    tests_require = ['WebTest']
    )