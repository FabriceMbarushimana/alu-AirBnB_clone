# alu-AirBnB_clone


## Description
This project is a simplified clone of the AirBnB web application, built using Python.
The first phase focuses on creating a command-line interpreter (console) that allows users to create, manage, serialize, and persist objects.

## The console is used to:
Create new objects (e.g., BaseModel, User)
Retrieve objects from storage
Update object attributes
Delete objects
Persist data using JSON file storage
This project helps build a strong foundation in object-oriented programming, data persistence, and backend architecture.

## Command Interpreter

### How to Start
To start the command interpreter, run:
```bash
./console.py
```

### How to Use
The command interpreter provides an interactive shell with the following commands:

- `create <class_name>` - Creates a new instance of the specified class
- `show <class_name> <id>` - Displays the string representation of an instance
- `destroy <class_name> <id>` - Deletes an instance based on class name and id
- `all [class_name]` - Lists all instances or instances of a specific class
- `update <class_name> <id> <attribute_name> "<attribute_value>"` - Updates an instance attribute
- `quit` or `EOF` - Exits the program
- `help` - Shows available commands

### Examples

#### Creating a new BaseModel instance:
```bash
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
```

#### Showing an instance:
```bash
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
```

#### Listing all instances:
```bash
(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
```

#### Updating an instance:
```bash
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "User_Name"
```

#### Creating a User:
```bash
(hbnb) create User
38f22813-2753-4d42-b37c-57a17f1e4f88
```

## Project Structure
```

alu-AirBnB_clone/
│
├── console.py
├── README.md
├── AUTHORS
├── file.json # auto-created
│
├── models/
│   ├── __init__.py
│   ├── base_model.py
│   ├── user.py
│   │
│   └── engine/
│       ├── __init__.py
│       └── file_storage.py
│
└── tests/
    ├── __init__.py
    ├── test_models/
    │   ├── __init__.py
    │   ├── test_base_model.py
    │   └── test_user.py
    │
    └── test_engine/
        ├── __init__.py
        └── test_file_storage.py

```

## Classes

### BaseModel
The base class for all other classes in the project. Provides common attributes and methods:
- `id`: Unique identifier (UUID4)
- `created_at`: Creation timestamp
- `updated_at`: Last update timestamp
- `save()`: Updates the `updated_at` attribute
- `to_dict()`: Returns dictionary representation

### User
Represents a user in the system:
- `email`: User's email address
- `password`: User's password
- `first_name`: User's first name
- `last_name`: User's last name
 
## Storage
The project uses JSON file storage for persistence. All instances are automatically saved to `file.json` when created, updated, or deleted.

## Testing
Run the test suite with:
```bash
python3 -m unittest discover tests
```
 
