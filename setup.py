from setuptools import setup, find_packages

# Read the README file and ensure correct encoding when reading it
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='nettoyage-de-code-legacy',
    version='0.1',
    packages=find_packages(),
    description='Un outil Python pour analyser et nettoyer le code hérité.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/votre-utilisateur/nettoyage-de-code-legacy',
    author='Votre Nom',
    author_email='votre.email@example.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)