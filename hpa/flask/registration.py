from flask import Flask, jsonify, request

registration = Flask(__name__)

tasks = [
    {
        'id': 1,
        'name': 'haibin',
        'title': 'Learn python'
    }
]

@registration.route('/hpa', methods=['GET'])
def get_hpa():
    return jsonify({'tasks': tasks})

@registration.route('/hpa', methods=['POST'])
def create_hpa():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'name' : 'weihong', 
        'title': request.json['title']
    }
    tasks.append(task)    
    return jsonify({'tasks': tasks})

@registration.route('/hpa/<int:task_id>', methods=['DELETE'])
def delete_hpa(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})

if __name__ == '__main__':
    registration.run()
