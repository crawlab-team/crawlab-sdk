from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='crawlab-sdk',
    version='0.0.3',
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
    install_requires=[
        'Click==7.0',
        'requests==2.22.0',
        'prettytable==0.7.2',
    ],
    entry_points={
        'console_scripts': [
            'crawlab=cli:main'
        ]
    }
)
