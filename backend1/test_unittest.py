import unittest
from unittest.mock import patch, Mock
#from backend import app, course, learning_journey, positions, registration, role, skill_rewarded, skill_set, skill, staff
#from positions1 import *
#from backend1 import course1, positions1
#from backend.invokes import invoke_http, all_route
import positions1


class TestBackend(unittest.TestCase):

    #set up only once at the start of running the test case
    @classmethod
    def setUpClass(cls):
        pass
    
    #tear down after all test case ran
    @classmethod
    def tearDownClass(cls):
        pass
    
    #run setup for every test case
    def setUp(self):
        self.pst = positions1.Positions(20, 'Software Developer')
        #self.pst = Positions(20, 'Software Developer')

    #run tear down for every end of test case
    def tearDown(self):
        self.pst = None

    def test_get_all_position(self):
        result = positions1.position_get_all()
        expected_result = {
            "code": 200,
            "data": {
                "positions": [
                {
                    "Position_ID": 20,
                    "Position_Name": "Software Developer"
                },
                ]
            }
            }
        self.assertEqual(result, expected_result)

    #test if existing position name can be added
    def test_add_position(self):
        with patch('positions1.create_new_position.request.get_json') as mocked_get:
            mocked_get.return_value = {10, 'Software Developer'}
            result = positions1.create_new_position('Software Developer')
            #result = create_new_position('Software Developer')
            expected_result = {
                        "code": 400,
                        "data": {
                            "Position_Name": 'Software Developer'
                        },
                        "message": "Position already exists."
                    }
            self.assertEqual(result, expected_result)

    # def test_add(self):
    #     result = course1.add(10,5)
    #     self.assertEqual(result, 15)




#allow us to run the whole test suite by running - python test_unittest.py
#UPDATE: don't have to cd test just run: python -m unittest test.test_unittest
if __name__ == '__main__':
    unittest.main()