from setuptools import setup
setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='Cucumber',
    url='https://github.com/Faulcry/cucumber',
    author='Reese Chaplin',
    author_email='rhchaplin@gmail.com',
    packages=['cucumber'],
    install_requires=['sys','pickle','pathlib','json'],
    version='0.1',
    license='MIT',
    description='A python repo for handling file pickling and unpickling to-and-from .bin to .json, simply. That\'s it.',
    long_description=open('README.md').read(),
)