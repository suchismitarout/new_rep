from nose.tools import assert_true,assert_equal,assert_is_none,assert_is_not_none,assert_in
import requests

def test_student_api_get_response():
    response = requests.get("http://127.0.0.1:5000/")
    assert_true(response.ok)

def test_get_student_by_id():
    response = requests.get("http://127.0.0.1:5000/getstudentbyid/16753")
    actual = response.json()
    expected = {"age":27,"id":16753,"loc":"delhi","name":"khirod","salary":42000}
    assert_equal(expected,actual)

def test_delete_student_by_id():
    response = requests.delete("http://127.0.0.1:5000/deletebyid/16753")
    response1 = requests.get("http://127.0.0.1:5000/getstudentbyid/16753")
    actual = response1.json()
    assert_is_none(actual)

def test_add_student():
    response = requests.post("http://127.0.0.1:5000/add_new_student", json={"name": "khirod", "age": 27, "id": 16753, "salary": 42000, "loc": "delhi"})
    response1 = requests.get("http://127.0.0.1:5000/getstudentbyid/16753")
    assert(response1.ok)





