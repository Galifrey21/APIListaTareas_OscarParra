from flask import Flask, jsonify, request
app = Flask(__name__)

# some_data={"name":"Bobby", "lastname":"Rixer"}
todos = [{"label":"Nueva tarea1","done":True},
         {"label":"Nueva tarea2","done":True},
         {"label":"Nueva tarea3","done":True},
         {"label":"Task","done":True}
         ]


@app.route('/todos', methods=['POST'])

def add_new_todo():
    request_body = request.json
    todos.append(request_body)
    return jsonify(todos)

@app.route('/todos', methods=['GET'])

def hello_world():
  return jsonify(todos)

@app.route('/todos/<int:position>',methods=['DELETE'])

def delete_todo(position):
    print("Esta es la posición a eliminar:", position)
    if 0 <= position < len(todos):  # Verifica que la posición sea válida
        todos.pop(position)  # Elimina el elemento en la posición dada
    return jsonify(todos)  # Devuelve la lista actualizada


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
