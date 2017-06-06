
from __future__ import absolute_import
from setuptools import setup

setup(name='iglu',
      version='0.1',
      description='iglu: an Image LookUp library',
      url='https://github.com/slizb/iglu',
      author='Bradley Sliz',
      author_email='bradsliz@gmail.com',
      license='Apache 2.0',
      packages=['iglu'],
      install_requires=['sklearn',
                        'pandas',
                        'numpy',
                        'requests',
                        'beautifulsoup4',
                        'lxml'
                        ],
      zip_safe=False)
