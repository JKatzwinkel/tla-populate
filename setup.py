try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

readme = ''

setup(
    long_description=readme,
    name='tla-ingest',
    version='0.1.0',
    description='Simple Python script for uploading a TLA corpus dump into a running TLA ES backend',
    python_requires='==3.*,>=3.8.0',
    author='AAEW',
    author_email='Katzwinkel@users.noreply.github.co',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'tla-ingest=tla_ingest:main',
            'tla-populate-backend=tla_ingest.populate_tla:main',
        ],
    },
    install_requires=[
        'docopt==0.*,>=0.6.2',
        'requests==2.*,>=2.23.0',
        'tqdm==4.*,>=4.45.0'
    ],
)
