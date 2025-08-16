from setuptools import setup, find_packages

# Lire le fichier README et garantir le bon encodage lors de sa lecture
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
    # Les métadonnées du package sont fournies ci-dessus pour que les utilisateurs sachent à quoi s'attendre
    keywords='code nettoyage, analyse code, outil python', # Ajout d'exemples de mots-clés pour la recherche du package
)