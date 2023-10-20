from flask import Flask, request, jsonify

app = Flask(__name__)
students = [
    {'id': 1, 'name': 'John', 'percentage': 25},
    {'id': 2, 'name': 'Aaron', 'percentage': 67},
    {'id': 3, 'name': 'Raju', 'percentage': 95},
    {'id': 4, 'name': 'Pinku', 'percentage': 92}
]

@app.route('/students', methods = ['GET'])
def get_students():
    return jsonify({'info': 'List of all students', 'data': students})

@app.route('/students/<int:student_id>', methods = ['PUT'])
def update_student(student_id):
    data = request.get_json()
    student = next((s for s in students if s['id'] == student_id), None)
    if student is None:
        return jsonify({'error': 'Student not found'})
    student.update(data)
    return jsonify({'info': 'Student updated', 'data': student})

@app.route('/students/<int:student_id>', methods = ['GET'])
def read_student(student_id):
    student = next((s for s in students if s['id'] == student_id), None)
    if student is None:
        return jsonify({'error': 'Student not found'})
    return jsonify({'info': 'Get student', 'data': student})

@app.route('/students', methods = ['POST'])
def create_student():
    data = request.get_json()
    student = {
        'id': data['id'],
        'name': data['name'],
        'percentage': data['percentage']
    }
    students.append(student)
    return jsonify({'info': 'Student created', 'data': student})

@app.route('/students/<int:student_id>', methods = ['DELETE'])
def delete_student(student_id):
    student = next((s for s in students if s['id'] == student_id), None)
    if student is None:
        return jsonify({'error': 'Student not found'})
    students.remove(student)
    return jsonify({'info': 'Student deleted', 'data': student})





if __name__ == '__main__':
    app.run(debug = False)