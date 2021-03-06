# Task List

About Task List. To be updated soon.

# Installation and Configuration
 
### Pre-Requisites:

**Note: Choose appropriate downloads depending on the OS**

- `Python` version 3 and above - [Link](https://www.python.org/downloads/) and `Pip`.

### Configuration:

**Note: Skip the below two steps if you have a virtual environment setup already.**
- `python3 -m venv venv` creates the virtual environment directory with the name `venv`.
- `source venv/bin/activate` activates the virtual environment and we are all set to work on.

### Running the application:
 
 - From the virtual environment run `pip install -r requirements.txt` which will pull in all the dependency required for the application to execute.
 - `python3 manage.py migrate` - creates the database migrations.
 - `python3 manage.py createsuperuser` - creates a super user by which we could access the admin portal.
 - `python3 manage.py runserver` - will start the server.

### Available Features:
- User registration
- Login 
- Update password
- List tasks
- Filter tasks
- Reset filters
- Add task
- Edit task
- Update task
- Read task in detail
- Delete task

### Sample screenshots

![Sign IN](static/images/screen-shots/sign-in.png "Sign In")


![Sign UP](static/images/screen-shots/sign-up.png "Sign Up")


![Forgot Password](static/images/screen-shots/forgot-password.png "Forgot Password")


![Task List](static/images/screen-shots/task-list-view.png "Task List")


![Filtered Task List](static/images/screen-shots/filtered-task-view.png "Filtered Task View")


![Add Task View](static/images/screen-shots/add-task-view.png "Add Task View")


![Edit Task View](static/images/screen-shots/edit-task-view.png "Edit Task View")


![Read More View](static/images/screen-shots/read-more-view.png "Read More View")