from setuptools import setup, find_packages

setup(
    name='invoice_calculator',
    version='0.1',
    packages=find_packages(),
    description='A simple invoice calculator',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/invoice_calculator',
    author='Your Name',
    author_email='your.email@example.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
