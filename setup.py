from setuptools import setup,find_packages 

setup( 
	name='song_recommender', 
	version='0.0.1', 
	author='Vishnu Shaji', 
	author_email='vishnushaji2602@gmail.com', 
	packages=find_packages(), 
	install_requires=[ 
		'numpy', 
		'pandas', 
        'seaborn'
	], 
) 
