# INVENTORY MANAGEMENT SYSTEM

An simple inventory management system that allows users to create an inventory,
add inventory stock and track the sales made.

## Installation

1.Clone Repo

```
https://github.com/KivutiBrian/InventoryManagementApp.git
```

2.Create Virtual Environment folder

```
python -m venv env
```

3.Activate virtual environment in parent directory of your "env"

For Linux systems and MAC

```
source env/bin/avtivate
```

For Windows

```
env\Scripts\activate.bat
```

4.Install requierements
```
pip install - r requirements.txt
```

5.Create a .env file and fill in  the following input variables
```
DEBUG=True
FLASK_APP=main.py
FLASK_ENV=development
SECRET_KEY=
SQLALCHEMY_TRACK_MODIFICATION=True
SQLALCHEMY_ECHO = True
SQLALCHEMY_DATABASE_URI = 

``` 

### Input variables
* SECRET_KEY : application database uri
* SQLALCHEMY_DATABASE_URI : eg for postgresql postgresql://scott:tiger@localhost/mydatabase

6.run the application
```
flask run
```

## Features
* SQLAlchemy
* Python-dotenv
* psycopg2

