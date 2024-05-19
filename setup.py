from setuptools import setup, find_packages

setup(
    name='fluo_raman_norm',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'contourpy',
        'cycler==0.12.1',
        'exceptiongroup==1.2.1',
        'fonttools==4.51.0',
        'iniconfig==2.0.0',
        'kiwisolver==1.4.5',
        'matplotlib',
        'mypy==1.10.0',
        'mypy-extensions==1.0.0',
        'numpy',
        'packaging==24.0',
        'pandas',
        'pillow==10.3.0',
        'plotly==5.22.0',
        'pluggy==1.5.0',
        'pyparsing==3.1.2',
        'pytest==8.2.0',
        'python-dateutil==2.9.0.post0',
        'pytz==2024.1',
        'six==1.16.0',
        'tenacity==8.3.0',
        'tk==0.1.0',
        'tomli==2.0.1',
        'typing-extensions==4.11.0',
        'tzdata==2024.1'
    ],
    dependency_links=[
        'git+https://github.com/jojorichard/Fluorescence_Raman_normalisation.git'
    ]
)