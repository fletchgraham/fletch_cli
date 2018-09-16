from setuptools import setup
setup(
    name = 'fletch_cli',
    version = '0.1.0',
    packages = ['fletch_cli', 'fletch_tools'],
    entry_points = {
        'console_scripts': [
            'fletch_cli = fletch_cli.main:main'
        ]
    })
