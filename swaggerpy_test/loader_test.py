#
# Copyright (c) 2013, Digium, Inc.
#

import unittest
import swaggerpy

from swaggerpy import SwaggerProcessor, load_file


class TestProcessor(SwaggerProcessor):
    def process_resource_listing(self, resources, context):
        resources['processed'] = True


class LoaderTest(unittest.TestCase):
    def test_simple(self):
        uut = load_file('test-data/1.1/simple/resources.json')
        self.assertEqual('1.1', uut['swaggerVersion'])
        decl = uut['apis'][0]['api_declaration']
        self.assertEqual(1, len(decl['models']))
        self.assertEqual(1, len(decl['models']['Simple']['properties']))

    def test_processor(self):
        uut = load_file('test-data/1.1/simple/resources.json',
                                  processors=[TestProcessor()])
        self.assertEqual('1.1', uut['swaggerVersion'])
        self.assertTrue(uut['processed'])

    def test_missing(self):
        try:
            load_file(
                'test-data/1.1/missing_resource/resources.json')
            self.fail("Expected load failure b/c of missing file")
        except IOError:
            pass


if __name__ == '__main__':
    unittest.main()
