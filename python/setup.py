from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='crawlab-sdk',
    version='0.6.b20211224_1500',
    packages=find_packages(),
    url='https://github.com/crawlab-team/crawlab-sdk',
    license='BSD-3-Clause',
    author='tikazyq',
    author_email='tikazyq@163.com',
    description='Python SDK for Crawlab',
    long_description=long_description,
    long_description_content_type="text/markdown",
    scripts=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'requests==2.22.0',
        'prettytable==0.7.2',
        'pathspec==0.8.0',
        'grpcio==1.39.0',
        'grpcio-tools==1.39.0',
        'grpc-interceptor-headers==0.1.0',
        'print-color==0.4.5',
    ],
    entry_points={
        'console_scripts': [
            'crawlab-cli=cli.main:main'
        ]
    }
)
