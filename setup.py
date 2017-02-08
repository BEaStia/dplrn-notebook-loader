from setuptools import setup, find_packages
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()
setup(
    name="dplrn-notebook-loader",
    version='0.0.1',
    url="http://dplrn.com",
    author="DeepLearn, Inc.",
    description="DeepLearn Notebook Loader Extensions",
    long_description=open('README.md').read(),
    # packages=find_packages(exclude=('tmp',)),
    install_requires=[
        'notebook'
    ],
    # scripts=['link_css.py']
)
