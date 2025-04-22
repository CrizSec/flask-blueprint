from flask import Blueprint, render_template, request, redirect
from app import db
from app.models.task_model import MyTask

task_bp = Blueprint('task', __name__)

@task_bp.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        current_task = request.form['content'].strip()
        if current_task:
            new_task = MyTask(content=current_task)
            try:
                db.session.add(new_task)
                db.session.commit()
                return redirect('/')
            except Exception as e:
                print(f"ERROR: {e}")
                return f"ERROR: {e}"
        else:
            return redirect('/')
    else:
        tasks = MyTask.query.order_by(MyTask.created).all()
        return render_template('index.html', tasks=tasks)

@task_bp.route('/delete/<int:id>')
def delete(id):
    delete_task = MyTask.query.get_or_404(id)
    try:
        db.session.delete(delete_task)
        db.session.commit()
        return redirect('/')
    except Exception as e:
        return f"ERROR: {e}"
