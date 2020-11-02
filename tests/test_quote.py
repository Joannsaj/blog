import unittest
from app.models import Quote

class QuoteTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Quote class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_quote = Quote('Joan',1234,'Python Must Be Crazy','https://something/something')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_quote,Quote))

