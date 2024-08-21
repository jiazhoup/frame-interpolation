from setuptools import setup, find_packages

setup(
    name = 'film',
    version = '0.1.0',
    url = '',
    description = '',
    packages = find_packages(include=('frame-interpolation/models/film_net/*',))
)
