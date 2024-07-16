from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Function to load todos from file
def load_todos(filename):
    try:
        with open(filename, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

# Function to save todos to file
def save_todos(filename, todos):
    with open(filename, "w") as file:
        for todo in todos:
            file.write(todo + "\n")

@app.route('/')
def index():
    filename = "todos.txt"
    todos = load_todos(filename)
    enumerated_todos = enumerate(todos, start=1)  # Start enumeration from 1
    return render_template('index.html', todos=enumerated_todos)

@app.route('/edit_todo/<int:number>', methods=['GET', 'POST'])
def edit_todo(number):
    filename = "todos.txt"
    todos = load_todos(filename)

    if request.method == 'POST':
        new_todo = request.form['todo'].strip()
        if new_todo:
            todos[number - 1] = new_todo  # Update the correct index
            save_todos(filename, todos)
            return redirect(url_for('index'))
    
    # Ensure the number is within the range of todos
    if 1 <= number <= len(todos):
        todo_to_edit = todos[number - 1]
        return render_template('edit.html', number=number, todo=todo_to_edit)
    else:
        return "Invalid todo number"

@app.route('/add_todo', methods=['POST'])
def add_todo():
    filename = "todos.txt"
    todo = request.form['todo'].strip()
    if todo:
        todos = load_todos(filename)
        todos.append(todo)
        save_todos(filename, todos)
    return redirect(url_for('index'))

@app.route('/delete_todo/<int:number>')
def delete_todo(number):
    filename = "todos.txt"
    todos = load_todos(filename)

    # Ensure the number is within the range of todos
    if 1 <= number <= len(todos):
        del todos[number - 1]  # Delete the correct index
        save_todos(filename, todos)
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
