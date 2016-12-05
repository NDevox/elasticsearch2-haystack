# encoding: utf-8
from __future__ import absolute_import

import os
import unittest
import warnings

import django

test_runner = None
old_config = None

os.environ['DJANGO_SETTINGS_MODULE'] = 'test.settings'

django.setup()

from django.conf import settings

warnings.simplefilter('ignore', Warning)


def setup():
    try:
        from elasticsearch import Elasticsearch, ElasticsearchException
    except ImportError:
        raise unittest.SkipTest("elasticsearch-py not installed.")

    es = Elasticsearch(settings.HAYSTACK_CONNECTIONS['elasticsearch']['URL'])
    try:
        es.info()
    except ElasticsearchException as e:
        raise unittest.SkipTest("elasticsearch not running on %r" % settings.HAYSTACK_CONNECTIONS['elasticsearch']['URL'], e)

    global test_runner
    global old_config

    from django.test.runner import DiscoverRunner

    test_runner = DiscoverRunner()
    test_runner.setup_test_environment()
    old_config = test_runner.setup_databases()


def teardown():
    test_runner.teardown_databases(old_config)
    test_runner.teardown_test_environment()
