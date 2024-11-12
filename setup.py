from setuptools import setup, find_namespace_packages

setup(
    name='async-helper',
    version='0.3.0',
    install_requires=[
        'pytest-asyncio@git+git://github.com/pytest-dev/pytest-asyncio.git#egg=pytest-asyncio'
    ],
    description='Async Helper Module',
    packages=find_namespace_packages(include=['prometheus.*', 'tests.*', 'scripts.*']),
    entry_points={
        'console_scripts': [
        ]
    }
)