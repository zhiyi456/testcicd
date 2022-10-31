# import unittest
from unittest.mock import patch, Mock
import flask
# import requests
from collections import namedtuple

import unittest
from flask import Flask,jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)


from learning_journey import LearningJourney

class Testlearning_journey(unittest.TestCase):

    def test_create_new_learning_journey(self):
        new_lj = LearningJourney(1, 'Data Analyst', 'Analytics Foundation', 217)
        self.assertEqual(new_lj.Staff_ID, 1)
        self.assertEqual(new_lj.Position_Name, 'Data Analyst')
        self.assertEqual(new_lj.Skill_Name, 'Analytics Foundation')
        self.assertEqual(new_lj.Course_ID, 217)

    def test_create_new_LJ_with_wrong_type(self):
        with self.assertRaises(TypeError):
            LearningJourney('one','Data Analyst', 'Analytics Foundation', 217)
    def test_create_new_LJ_with_wrong_type2(self):
        with self.assertRaises(TypeError):
            LearningJourney(1,['Data Analyst'], 'Analytics Foundation', 217)
    def test_create_new_LJ_with_wrong_type3(self):
        with self.assertRaises(TypeError):
            LearningJourney(1,'Data Analyst', {'Analytics Foundation'}, 217)
    def test_create_new_LJ_with_wrong_type4(self):
        with self.assertRaises(TypeError):
            LearningJourney(1,'Data Analyst', 'Analytics Foundation', 'IS217')

    def test_create_new_LJ_with_wrong_type_error_msg(self):
        with self.assertRaises(TypeError) as e:
            LearningJourney('one','Data Analyst', 'Analytics Foundation', 217)
        msg = e.exception
        self.assertEqual(str(msg), "Staff_ID must be an integer")
    
    def test_create_new_LJ_with_wrong_type_error_msg2(self):
        with self.assertRaises(TypeError) as e:
            LearningJourney(1,['Data Analyst'], 'Analytics Foundation', 217)
        msg = e.exception
        self.assertEqual(str(msg), "Position_Name must be an integer")

    def test_create_new_LJ_with_wrong_type_error_msg3(self):
        with self.assertRaises(TypeError) as e:
            LearningJourney(1,'Data Analyst', {'Analytics Foundation'}, 217)
        msg = e.exception
        self.assertEqual(str(msg), "Skill_Name must be a string")

    def test_create_new_LJ_with_wrong_type_error_msg4(self):
        with self.assertRaises(TypeError) as e:
            LearningJourney(1,'Data Analyst', 'Analytics Foundation', 'IS217')
        msg = e.exception
        self.assertEqual(str(msg), "Course_ID must be an integer")

    def test_LJ_json(self):
        new_lj = LearningJourney(1, 'Data Analyst', 'Analytics Foundation', 217).json()
        self.assertEqual(new_lj, {'Learning_Journey_ID': None,
                                'Staff_ID':1,
                                'Position_Name': 'Data Analyst',
                                'Skill_Name': 'Analytics Foundation',
                                'Course_ID': 217})
       

from positions import Positions

class TestPositions(unittest.TestCase):
    
    def test_create_new_position(self):
        new_position = Positions('Data Analyst')
        self.assertEqual(new_position.Position_Name, 'Data Analyst')

    def test_create_new_position_with_wrong_type(self):
        with self.assertRaises(TypeError):
            Positions(1)

    def test_create_new_position_with_wrong_type_error_msg(self):
        with self.assertRaises(TypeError) as e:
            Positions(1)
        msg = e.exception
        self.assertEqual(str(msg), "Position_Name must be a string")

    def test_position_json(self):
        new_position = Positions('Data Analyst').json()
        self.assertEqual(new_position, {'Position_Name': 'Data Analyst'})

from skill_rewarded import Skill_Rewarded

class TestSkill_Rewarded(unittest.TestCase):
    
    def test_create_new_SR(self):
        new_SR = Skill_Rewarded(1, 'Analytics', 217)
        self.assertEqual(new_SR.Skill_Rewarded_ID, 1)
        self.assertEqual(new_SR.Skill_Name, 'Analytics')
        self.assertEqual(new_SR.Course_ID, 217)

    def test_create_new_SR_with_wrong_type(self):
        with self.assertRaises(TypeError):
            Skill_Rewarded('one', 'Analytics', 217)
    def test_create_new_SR_with_wrong_type2(self):
        with self.assertRaises(TypeError):
            Skill_Rewarded(1, ['Analytics'], 217)
    def test_create_new_SR_with_wrong_type3(self):
        with self.assertRaises(TypeError):
            Skill_Rewarded(1, 'Analytics', 'IS217')

    def test_create_new_SR_with_wrong_type_error_msg(self):
        with self.assertRaises(TypeError) as e:
            Skill_Rewarded('one', 'Analytics', 217)
        msg = e.exception
        self.assertEqual(str(msg), "Skill_Rewarded_ID must be an integer")
    def test_create_new_SR_with_wrong_type_error_msg2(self):
        with self.assertRaises(TypeError) as e:
            Skill_Rewarded(1, ['Analytics'], 217)
        msg = e.exception
        self.assertEqual(str(msg), "Skill_Name must be a string")
    def test_create_new_SR_with_wrong_type_error_msg3(self):
        with self.assertRaises(TypeError) as e:
            Skill_Rewarded(1, 'Analytics', 'IS217')
        msg = e.exception
        self.assertEqual(str(msg), "Course_ID must be an integer")

    def test_SR_json(self):
        new_SR = Skill_Rewarded(1, 'Analytics', 217).json()
        self.assertEqual(new_SR, {"Skill_Rewarded_ID": 1, 
                                "Skill_Name": 'Analytics',
                                "Course_ID": 217})

from skill_set import Skill_Set

class TestSkill_Set(unittest.TestCase):
    
    def test_create_new_SS(self):
        new_ss = Skill_Set('Analytics', 'Data Analyst')
        self.assertEqual(new_ss.Skill_Name, 'Analytics')
        self.assertEqual(new_ss.Position_Name, 'Data Analyst')

    def test_create_new_SS_with_wrong_type(self):
        with self.assertRaises(TypeError):
            Skill_Set(['Analytics'], 'Data Analyst')
    def test_create_new_SS_with_wrong_type2(self):
        with self.assertRaises(TypeError):
            Skill_Set('Analytics', 217)

    def test_create_new_SS_with_wrong_type_error_msg(self):
        with self.assertRaises(TypeError) as e:
            Skill_Set(['Analytics'], 'Data Analyst')
        msg = e.exception
        self.assertEqual(str(msg), "Skill_Name must be a string")
    def test_create_new_SS_with_wrong_type_error_msg2(self):
        with self.assertRaises(TypeError) as e:
            Skill_Set('Analytics', 217)
        msg = e.exception
        self.assertEqual(str(msg), "Position_Name must be a string")

    def test_SS_json(self):
        new_ss = Skill_Set('Analytics', 'Data Analyst').json()
        self.assertEqual(new_ss, {"Skill_Set_ID": None, 
                                        "Skill_Name": 'Analytics', 
                                        "Position_Name": 'Data Analyst'})
    
from skill import Skill

class TestSkill(unittest.TestCase):
    def test_create_new_skill(self):
        new_skill = Skill('Analytics')
        self.assertEqual(new_skill.Skill_Name, 'Analytics')

    def test_create_new_skill_with_wrong_type(self):
        with self.assertRaises(TypeError):
            Skill(217)

    def test_create_new_skill_with_wrong_type_error_msg(self):
        with self.assertRaises(TypeError) as e:
            Skill(217)
        msg = e.exception
        self.assertEqual(str(msg), "Skill_Name must be a string")

    def test_skill_json(self):
        new_skill = Skill('Analytics').json()
        self.assertEqual(new_skill, {'Skill_Name': 'Analytics'})

#allow us to run the whole test suite by running - python test_unittest.py
#UPDATE: don't have to cd test just run: python -m unittest test.test_unittest
if __name__ == '__main__':
    unittest.main()

    # def test_position_get_all(self):
    #     with app.app_context():
    #         with patch('positions1.Positions') as mocked_get:
    #             # inst1 = positions1.Positions(1, "Data Analyst")
    #             # inst2 = positions1.Positions(2, "Human Resource")
    #             # inst3 = positions1.Positions(3, "Head of Security")
    #             #mock_return = [positions1.Positions(1, "Data Analyst"), positions1.Positions(2, "Human Resource"), positions1.Positions(3, "Head of Security")]
                
    #             mock_data = [
    #                 {   
    #                 "Position_ID": 1,
    #                 "Position_Name": "Data Analyst"
    #                 },
    #                 {
    #                 "Position_ID": 2,
    #                 "Position_Name": "Human Resource"
    #                 },
    #                 {
    #                 "Position_ID": 3,
    #                 "Position_Name": "Head of Security"
    #                 }]
    #             #print(mock_return)
    #             #converting dictionary to objects to simulate db
    #             mock_return = []
    #             for data in mock_data:
    #                 object_name = namedtuple("ObjectName", data.keys())(*data.values())
    #                 mock_return.append(object_name)
    #             expected_result = flask.jsonify({
    #                 "code": 200,
    #                 "data": {
    #                     "positions": [
    #                     {
    #                         "Position_ID": 1,
    #                         "Position_Name": "Data Analyst"
    #                     },
    #                     {
    #                         "Position_ID": 2,
    #                         "Position_Name": "Human Resource"
    #                     },
    #                     {
    #                         "Position_ID": 3,
    #                         "Position_Name": "Head of Security"
    #                     }
    #                     ]
    #                 }
    #                 })
    #             mocked_get.query.all.return_value = mock_return
    #             result = positions.position_get_all()
    #             # print(fake_return)
    #             #print(result)
    #             self.maxDiff = None
    #             self.assertEqual(result.data, expected_result.data)

    # def test_position_by_name(self):
    #     with app.app_context():
    #         with patch('positions1.Positions') as mocked_get:
    #             # inst1 = positions1.Positions(1, "Data Analyst")
    #             # inst2 = positions1.Positions(2, "Human Resource")
    #             # inst3 = positions1.Positions(3, "Head of Security")
    #             #mock_return = [positions1.Positions(1, "Data Analyst"), positions1.Positions(2, "Human Resource"), positions1.Positions(3, "Head of Security")]
    #             mock_data = [
    #                 {   
    #                 "Position_ID": 1,
    #                 "Position_Name": "Data Analyst"
    #                 }]
    #             #print(mock_return)
    #             #converting dictionary to objects to simulate db
    #             mock_return = []
    #             for data in mock_data:
    #                 object_name = namedtuple("ObjectName", data.keys())(*data.values())
    #                 mock_return.append(object_name)
    #             expected_result = flask.jsonify({
    #                 "code": 200,
    #                 "data": {
    #                     "Positions": [
    #                     {
    #                         "Position_ID": 1,
    #                         "Position_Name": "Data Analyst"
    #                     }
    #                     ]
    #                 }
    #                 })
    #             mocked_get.query.filter_by.return_value = mock_return
    #             result = positions.get_position_by_name("Data Analyst")
    #             # print(fake_return)
    #             print(result)
    #             self.maxDiff = None
    #             self.assertEqual(result.data, expected_result.data)

    # def test_position_by_ID(self):
    #     with app.app_context():
    #         with patch('positions1.Positions') as mocked_get:
    #             # inst1 = positions1.Positions(1, "Data Analyst")
    #             # inst2 = positions1.Positions(2, "Human Resource")
    #             # inst3 = positions1.Positions(3, "Head of Security")
    #             #mock_return = [positions1.Positions(1, "Data Analyst"), positions1.Positions(2, "Human Resource"), positions1.Positions(3, "Head of Security")]
    #             mock_data = [
    #                 {   
    #                 "Position_ID": 1,
    #                 "Position_Name": "Data Analyst"
    #                 }]
    #             #print(mock_return)
    #             #converting dictionary to objects to simulate db
    #             mock_return = []
    #             for data in mock_data:
    #                 object_name = namedtuple("ObjectName", data.keys())(*data.values())
    #                 mock_return.append(object_name)
    #             expected_result = flask.jsonify({
    #                 "code": 200,
    #                 "data": {
    #                     "Positions": [
    #                     {
    #                         "Position_ID": 1,
    #                         "Position_Name": "Data Analyst"
    #                     }
    #                     ]
    #                 }
    #                 })
    #             mocked_get.query.filter_by.return_value = mock_return
    #             result = positions.get_position_by_ID(1)
    #             # print(fake_return)
    #             print(result)
    #             self.maxDiff = None
    #             self.assertEqual(result.data, expected_result.data)