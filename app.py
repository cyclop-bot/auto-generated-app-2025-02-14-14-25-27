from flask import Flask, request, jsonify

app = Flask(__name__)

todos = []

def add_todo(todo):
    todos.append(todo)

@app.route('/todos', methods=['POST'])
def create_todo():
    todo = request.json['todo']
    add_todo(todo)
    return jsonify({'message': 'Todo created successfully'})

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify({'todos': todos})

if __name__ == '__main__':
    app.run(debug=True)