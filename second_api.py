from flask import Flask, request,jsonify
import json
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

USER_DATA = {"admin": "superpw"}
@auth.verify_password
def verify(username, password):
    if not (username and password):
        return False
    return USER_DATA.get(username) == password

with open("C:/Users/Ranjitha/PycharmProject/rest_api_prj/student_data.py", "r") as fp:
    content = fp.read()
    d = content.split("\n")
    # print(d)
    res = [json.loads(i) for i in d if len(i) > 0]
    # print(res)


@app.route('/', methods=['GET'])
@auth.login_required
def get_student_info():
    return jsonify(res)


@app.route('/getstudentbyid/<int:id>', methods=['GET'])
@auth.login_required
def get_student_info_by_id(id):
    data = None
    for i in res:
        if i["id"] == id:
            data = i
    return jsonify(data)


@app.route('/deletebyid/<int:id>', methods=['DELETE'])
@auth.login_required
def delete_by_student_by_id(id):
    for i in res:
        if i["id"] == id:
            res.remove(i)
    return jsonify(res)


@app.route('/add_new_student', methods=['POST'])
@auth.login_required
def add_new_student():
    name = request.form.get("name")
    age = request.form.get("age")
    id = request.form.get("id")
    salary = request.form.get("salary")
    loc = request.form.get("loc")
    d = {"name": name, "age": age, "id": id, "salary": salary, "loc": loc}
    data = request.get_json(d)
    res.append(data)
    with open ("C:/Users/Ranjitha/PycharmProject/rest_api_prj/student_data.py", "w") as fw:
        for i in res:
            fw.write(json.dumps(i))
            fw.write("\n")

    return jsonify(res)


if __name__ =='__main__':
    app.run()









