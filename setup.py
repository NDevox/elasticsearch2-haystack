from __future__ import unicode_literals

import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='elasticsearch2-haystack',
    version='0.1',
    description='An elasticsearch2 compatible backend for Haystack',
    long_description=read('README.rst'),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
        'Framework :: Django',
    ],
    author='Nick Sarbicki',
    author_email='nick.a.sarbicki@gmail.com',
    url='http://github.com/ndevox/elasticsearch2-haystack',
    download_url='http://github.com/ndevox/elasticsearch2-haystack/tarball/0.1',
    license='GPL2',
    py_modules=['elasticsearch2_backend'],
    install_requires=[
        'django-haystack>=2',
        'elasticsearch<5'
    ]
)
