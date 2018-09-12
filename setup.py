from setuptools import setup
setup(
    name = 'pycli',
    version = '0.1.0',
    packages = ['fletch_cli'],
    entry_points = {
        'console_scripts': [
            'fletch_cli = fletch_cli.main:main'
        ]
    })