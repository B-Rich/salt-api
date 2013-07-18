# utf-8
'''
Test blah
'''
import cherrypy

from cptestcase import BaseCherryPyTestCase

from app import Root

def setUpModule():
    cherrypy.tree.mount(Root(), '/')
    cherrypy.engine.start()
setup_module = setUpModule

def tearDownModule():
    cherrypy.engine.exit()
teardown_module = tearDownModule

class TestCherryPyApp(BaseCherryPyTestCase):
    def test_index(self):
        response = self.request('/')
        self.assertEqual(response.output_status, '200 OK')
        # response body is wrapped into a list internally by CherryPy
        self.assertEqual(response.body, ['hello world'])

    def test_echo(self):
        response = self.request('/echo', msg="hey there")
        self.assertEqual(response.output_status, '200 OK')
        self.assertEqual(response.body, ["hey there"])

        response = self.request('/echo', method='POST', msg="back from the future")
        self.assertEqual(response.output_status, '200 OK')
        self.assertEqual(response.body, ["back from the future"])

if __name__ == '__main__':
    import unittest
    unittest.main()
