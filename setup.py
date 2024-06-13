from setuptools import find_packages,setup
from typing import List

HYPHEN = '-e .'
def get_requirements(filename:str)->List[str]:
    requirements=[]
    with open(filename) as f:
        requirements= f.readlines()
        requirements=[req.replace('\n','') for req in requirements]

        if HYPHEN in requirements:
            requirements.remove(HYPHEN)

    return requirements

setup(
    name='MLprojects',
    version='3.12.3',
    author='Vivek',
    author_email='mastervivek23@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)