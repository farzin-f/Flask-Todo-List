from alayatodo import app
from flask import (
    g,
    redirect,
    render_template,
    request,
    session,
    jsonify
    )
from werkzeug.security import (
    generate_password_hash,
    check_password_hash
    )

from .models import db, User, Todo

@app.route('/')
def home():
    with app.open_resource('../README.md', mode='r') as f:
        readme = "".join(l.decode('utf-8') for l in f)
        return render_template('index.html', readme=readme)


@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login_POST():
    username = request.form.get('username')
    password = request.form.get('password')

    user = User.query.filter_by(username=username).first_or_404()
        
    if user and check_password_hash(user.password, password):
        session['user'] = {
            "id": user.id,
            "username": user.username
            }
        session['logged_in'] = True
        return redirect('/todo')

    return redirect('/login')


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('user', None)
    return redirect('/')


@app.route('/todo/<id>', methods=['GET'])
def todo(id):
    todo = Todo.query.get_or_404(id)
    return render_template('todo.html', todo=todo)

@app.route('/todo/<id>/json', methods=['GET'])
def todo_json(id):
    todo = Todo.query.get_or_404(id)

    return todo.to_json()
    

@app.route('/todo', methods=['GET'])
@app.route('/todo/page/<int:page>', methods=['GET'])
def todos(page=1):
    if not session.get('logged_in'):
        return redirect('/login')

    # getting the paginated records
    todos = Todo.query.paginate(
        per_page=2, page=page, error_out=True)

    return render_template('todos.html', todos=todos)


@app.route('/todo', methods=['POST'])
@app.route('/todo/', methods=['POST'])
def todos_POST():
    if not session.get('logged_in'):
        return redirect('/login')
    
    user_id = session['user']['id']
    description = request.form.get('description')
    page = int(request.form.get('page'))
    
    todo = Todo(description=description, user_id=user_id)
    db.session.add(todo)
    db.session.commit()

    todos = Todo.query.paginate(
        per_page=2, page=page, error_out=True)
    # rendering the pagination template to populate the
    # lates version for the view
    pagination_html = render_template('pagination.html', todos=todos)
        
    return jsonify(pagination_html)
    
@app.route('/todo/<id>/update', methods=['POST'])
@app.route('/todo/<id>/update/', methods=['POST'])
def todo_update(id):
    id = request.form.get('todoId')
    is_completed = request.form.get('is_completed')

    todo = Todo.query.get_or_404(id)
    todo.is_completed = is_completed
    db.session.commit()
    
    return jsonify(completed=todo.is_completed)
        
@app.route('/todo/<id>/delete', methods=['POST'])
def todo_delete(id):
    if not session.get('logged_in'):
        return redirect('/login')

    page = int(request.form.get('page'))
        
    todo = Todo.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()

    # getting the total number of pages after deletion
    todos = Todo.query.paginate(
        per_page=2, page=1, error_out=True)

    # if the actual page is greater that the pages after deletion
    # the view should display the new total pages
    if page > todos.pages:
        page = todos.pages
    
    todos = Todo.query.paginate(
        per_page=2, page=page, error_out=True)
    # rendering the pagination template to populate the
    # lates version for the view
    pagination_html = render_template('pagination.html', todos=todos)
    
    return jsonify(pagination_html)
