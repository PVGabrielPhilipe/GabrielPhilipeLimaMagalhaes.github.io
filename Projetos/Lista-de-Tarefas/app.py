from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# Lista global para armazenar tarefas
tasks = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_task', methods=['POST'])
def add_task():
    task = request.form['task']
    tasks.append(task)
    return redirect(url_for('tasks_page'))

@app.route('/tasks')
def tasks_page():
    return render_template('tasks.html', tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)
