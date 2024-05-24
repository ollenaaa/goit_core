from setuptools import setup

setup(
    name='Folder_Cleaner',
    version='1.0',
    description='Useful folder cleaner',
    url='https://github.com/ollenaaa/goit_core',
    author='Olena Sazonets',
    author_email='elenasazonets@gmail.com',
    license='MIT',
    packages=['clean_folder'],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'clean-folder = clean_folder.clean:main'
        ]
    },
)
