Alayacare Python skill test
===========================


### Application
The TODO App allows a user to add reminders of thing he needs to do. Here are the requirement for the app.
* Users can add, delete and see their todos.
* All the todos are private, users can't see other user's todos.
* Users must be logged in order to add/delete/see their todos.

Credentials:
* username: **user1**
* password: **user1**

#### Homepage:
![Homepage](/web/img/homepage.png?raw=true "Homepage")

#### Login page:
![Login page](/web/img/login-page.png?raw=true "Login page")

#### Todos:
![Todos](/web/img/todos.png?raw=true "Todos")

### Requirements
* python 5.7
* virtualenv
* sqlite3
* A github account

### Installation
**/!\ You need to fork this repository. See [How to submit your work?](#how-to-submit-your-work)**
```sh
virtualenv .
bin/pip install -r requirements.txt
bin/python main.py initdb
bin/python main.py
```

### Tasks
* TASK 1: As a user I can't add a todo without a description.
  - The confirmation is being done through JavaScript and in the
  front-end to decrease the server traffic (ref:
  ```static/js/todos.js```).
* TASK 2: As a user I can mark a todo as completed.
  - A is_completed column added to the todo model which will be
  updated each time the user toggle the Done checkbox. (ref: ```alaytodo/models.py```).
* TASK 3: As a user I can view a todo in a JSON format.
  - The todo_json has been added to the view controller in
  ```alaytodo/views.py``` which return the JSON object.
* TASK 4: As a user I can see a confirmation message when I add/delete
  a todo.
  - The confirmation messages are being handled in front-end using
  ```showAlert()``` function which triggers for
  addition/deletion/ and description confirmation of a todo.
* TASK 5: As a user I can see my list of todos paginated.
* TASK 6: Implement an ORM database access layer so we don’t have SQL
  in the controller code.
  - Tasks 5 and 6 are done using Flask SQLAlchemy
  extension. Models have been created in
  ```alaytodo/models.py```. The pagination is being done
  through the SQLAlchemy model utilities for this purpose and
  being called in ```todos()``` function (```alaytodo/views.py```).

Extra tasks:
- Fix any bug you may find.
  - I couldn't find any significant bug.
- Fix any security issue you may find.
  - For the password I added the encryption using werkzeug.security library.

### Documentation
This app use [Flask](http://flask.pocoo.org/docs/0.10/).

