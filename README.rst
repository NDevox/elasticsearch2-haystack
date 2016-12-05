===================================
Elasticsearch 2 Engine for Haystack
===================================

:author: Nick Sarbicki
:date: 2016/12/05
.. image:: https://travis-ci.org/NDevox/elasticsearch2-haystack.svg?branch=master
    :target: https://travis-ci.org/NDevox/elasticsearch2-haystack

This is a fairly hacked together Elasticsearch backend for haystack which supports
all versions of Elasticsearch up to 2.4.

This is strongly based on the original haystack Elasticsearch backend and essentially
just patches breaking changes from Elasticsearch 2 to replicate the functionality from
Elasticsearch 1.

Requirements
============

The requirements of this project largely match those of Haystack (except you can use Elasticsearch 2).

You can find these here: http://django-haystack.readthedocs.io/en/latest/#requirements

Otherwise it will require the appropriate elasticsearch-py installation. In this case the major
version must match the version of elasticsearch you are using.

In general the project supports Python 2.7 and 3.4+.

Installation
============

To run this engine in haystack you need to set your connections settings with the ``ENGINE``
variable as so:

.. code-block:: python

    HAYSTACK_CONNECTIONS = {
        'default': {
            'ENGINE': 'elasticsearch2_backend.ElasticsearchSearchEngine',
            'URL': 'http://127.0.0.1:9200/',
            'INDEX_NAME': 'haystack',
        },
    }

===========
Development
===========

The tests from haystack for the elasticsearch engine have been ported over. To run these make sure
you have nose installed (see the ``test-requirements.txt`` file) and then run
``nosetests -v --with-coverage --cover-package=elasticsearch2_backend``.
