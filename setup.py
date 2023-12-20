from setuptools import setup, find_packages

# Read the contents of your requirements.txt file
with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='board',
    version='0.1',
    packages=find_packages(),
    install_requires=required,
    # Optional
    author='Santosh KV',
    author_email='gyannetics@gmail.com',
    description='A simple demonstration of a message board using Python and Flask',
    license='MIT',
    url='https://github.com/gyannetics/message-board',
    # More metadata
)
