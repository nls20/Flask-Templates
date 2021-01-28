from flask import render_template, request, redirect
from app import app
from app.models.todo_list import tasks
from app.models.task import *

@app.route('/tasks')
def index():
    return render_template('index.html', title='Home', tasks=tasks)


@app.route('/tasks', methods=['POST'])
def add_task():
    task_title = request.form["title"]
    task_description = request.form["description"]
    new_task = Task(task_title, task_description, False)
    tasks.append(new_task)
    return redirect('/tasks')