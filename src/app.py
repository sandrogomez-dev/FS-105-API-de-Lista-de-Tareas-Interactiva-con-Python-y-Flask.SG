from flask import Flask, jsonify, request, abort

app = Flask(__name__)

todos = [ { "label": "My first task", "done": False } ]

@app.route('/todos', methods=['GET'])
def get_todos():
    """Endpoint para obtener todas las tareas"""
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    """Endpoint para agregar una nueva tarea"""
    request_body = request.json
    
    if not request_body or 'label' not in request_body:
        abort(400, description="Falta el campo 'label' en el request")
    
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return jsonify(todos), 201 

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    """Endpoint para eliminar una tarea por su posición"""
    print("This is the position to delete:", position)
    
    
    if position < 0 or position >= len(todos):
        abort(404, description="Posición no encontrada")
    
    todos.pop(position)
    return jsonify(todos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)