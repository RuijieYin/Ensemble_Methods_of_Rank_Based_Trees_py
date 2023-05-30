from setuptools import setup, find_packages

VERSION = '0.1.1' 
DESCRIPTION = 'A Python package for Ensemble Methods of Rank-Based Trees'
LONG_DESCRIPTION = 'This package contains several essential functions to implement Ensemble Methods of Rank-Based Trees in Python'

# Setting up
setup(
       # the name must match the folder name 'EnsembleRankTrees'
        name="EnsembleRankTrees", 
        version=VERSION,
        author="Ruijie Yin",
        author_email="<ruijieyin428@gmail.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=["pandas", "sklearn", "numpy", "shap-hypetune", "lightgbm"], # add any additional packages that 
        # needs to be installed along with your package. 
        
        keywords=['python', 'ensemble','rank-based'],
        classifiers= [
            "Programming Language :: Python :: 3.9.1",
            "Operating System :: OS Independent"
        ]
)