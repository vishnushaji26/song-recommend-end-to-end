from setuptools import setup,find_packages 
from typing import list

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of required libraries
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup( 
	name='song_recommender', 
	version='0.0.1', 
	author='Vishnu Shaji', 
	author_email='vishnushaji2602@gmail.com', 
	packages=find_packages(), 
	install_requires=get_requirements('requirements.txt')
) 
