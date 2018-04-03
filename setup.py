from setuptools import setup, find_packages
from codecs import open  # To use a consistent encoding
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()
    
version = '0.0.1'

setup(
    name='''ckanext-tableauview''',
    version=version,
    description='''CKAN Tableau Public ResourceView''',
    long_description=''' ''',

    url='http://github.com/geosolutions-it/ckanext-tableauview',

    author='''Emanuele Tajariol''',
    author_email='''etj@geo-solutions.it''',

    license='AGPL',
    
    classifiers=[
        # How mature is this project? Common values are
        # 3 - Alpha
        # 4 - Beta
        # 5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2.7'
    ],
    keywords='''tableau view''',
    
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),    
    namespace_packages=['ckanext', 'ckanext.tableauview'],
    
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''
       [ckan.plugins]
       tableau_view=ckanext.tableauview.plugin:TableauView    
    ''',
)
