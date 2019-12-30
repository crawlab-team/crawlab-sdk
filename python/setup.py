from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='crawlab-sdk',
    version='0.0.1',
    packages=['core', 'cli', 'constants'],
    url='https://github.com/crawlab-team/crawlab-sdk',
    license='BSD-3-Clause',
    author='tikazyq',
    author_email='tikazyq@163.com',
    description='SDK for Crawlab',
    long_description=long_description,
    scripts=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'crawlab=cli:main'
        ]
    }
)
