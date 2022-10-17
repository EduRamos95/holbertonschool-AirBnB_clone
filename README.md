# AirBnB Clone - The Console

<p align="center">
<img src="https://cloudfront-us-east-1.images.arcpublishing.com/infobae/UEZCFF3XMJF3XHZX5YIM5D735E.jpeg" width="700px" height="420px" padding="auto" ></img>
</p>

The console is the first segment of the AirBnB project at Holberton School that will collectively cover fundamental concepts of higher level programming. The goal of AirBnB project is to eventually deploy our server a simple copy of the AirBnB Website(HBnB). A command interpreter is created in this segment to manage objects for the AirBnB(HBnB) website.

<p align="center">
<img src="https://raw.githubusercontent.com/DaisyGeraldine/holbertonschool-AirBnB_clone/master/AirBnB%20clone%20%29.png" width="700px" height="350px" ></img>
</p>

#### Functionalities of this command interpreter:
* Create a *`new object`* (ex: a new `User` or a new `Place`)
* Retrieve an *`object from a file, a database etc...`*
* Show an *`object`*
* Display *`all objects`* or *`objects in specific Class`*
* Update *`attributes of an object`*
* Destroy an *`object`*

## Table of Content
* [Environment](#environment)
* [Installation](#installation)
* [File Descriptions](#file-descriptions)
* [Examples of use](#examples-of-use)
* [Bugs](#bugs)
* [Authors](#authors)

## Environment
This project is interpreted on Ubuntu 20.04 LTS using python3 (version 3.8.5)

## Installation
* Clone this repository: **`git clone "git@github.com:EduRamos95/holbertonschool-AirBnB_clone.git"`**
* Access AirBnb directory: **`cd holbertonschool-AirBnB_clone`**
* Run hbnb(interactively): **`./console`** and enter command
* Run hbnb(non-interactively): **`echo "<command>" | ./console.py`**

## File Descriptions
[**`console.py`**](https://github.com/EduRamos95/holbertonschool-AirBnB_clone/blob/main/console.py) - the console contains the entry point of the command interpreter.
List of commands this console current supports:
* **`EOF`** - exits console
* **`quit`** - exits console
* **`<emptyline>`** - overwrites default emptyline method and does nothing
* **`create`** - Creates a new instance of (*`BaseModel`*, *`User`* , *`Place`*, *`etc...`*), **saves it** (to the **JSON file**) and **prints the id**
* **`destroy`** - Deletes an instance based on the `<class name>` and `<id>` (**save the change** into the **JSON file**).
* **`show`** - Prints the string representation of an instance based on the `<class name>` and `<id>`.
* **`all`** - Prints all string representation of all instances based or not on the `<class name>`.
* **`update`** - Updates an instance based on the `<class name>` and `<id>` by adding or updating `<attribute>` and `<value>` (**save the change** into the **JSON file**).

#### `models/` directory contains classes used for this project:
[**`base_model.py`**](https://github.com/EduRamos95/holbertonschool-AirBnB_clone/blob/main/models/base_model.py) - The BaseModel class from which future classes will be derived
* **`def __init__(self, *args, **kwargs)`** - Initialization of the base model
* **`def __str__(self)`** - String representation of the BaseModel class
* **`def save(self)`** - Updates the attribute *`updated_at`* with the current datetime
* **`def to_dict(self)`** - returns a dictionary containing all keys/values of the instance

Classes inherited from Base Model:
* [*`amenity.py`*](https://github.com/EduRamos95/holbertonschool-AirBnB_clone/blob/main/models/amenity.py)
* [*`city.py`*](https://github.com/EduRamos95/holbertonschool-AirBnB_clone/blob/main/models/city.py)
* [*`place.py`*](https://github.com/EduRamos95/holbertonschool-AirBnB_clone/blob/main/models/place.py)
* [*`review.py`*](https://github.com/EduRamos95/holbertonschool-AirBnB_clone/blob/main/models/review.py)
* [*`state.py`*](https://github.com/EduRamos95/holbertonschool-AirBnB_clone/blob/main/models/state.py)
* [*`user.py`*](https://github.com/EduRamos95/holbertonschool-AirBnB_clone/blob/main/models/user.py)

#### `/models/engine` directory contains File Storage class that handles JASON serialization and deserialization :
[**`file_storage.py`**](https://github.com/EduRamos95/holbertonschool-AirBnB_clone/blob/main/models/engine/file_storage.py) - serializes instances to a JSON file & deserializes back to instances
* **`def all(self)`** - returns the dictionary  **__objects**
* **`def new(self, obj)`** - sets in **__objects** the obj with **key** `"<class name>.<id>"`
* **`def save(self)`** - serializes **__objects to the JSON file** (path: __file_path)
* **` def reload(self)`** -  deserializes the **JSON file to __objects**

#### `/tests` directory contains all unit test cases for this project:
[**`/test_models/test_base_model.py`**](/tests/test_models/test_base_model.py) - Contains the TestBaseModel and TestBaseModelDocs classes.
TestBaseModelDocs class:
* (in maintance)

## Examples of use
```py
root@DESKTOP-F800J0P:~/FullStack-EDU/holbertonschool-AirBnB_clone# ./console.py
(hbnb) all MyModel
** class doesn't exist **
(hbnb) show BaseModel
** instance id missing **
(hbnb) show BaseModel My_First_Model
** no instance found **
(hbnb) create BaseModel
5e21da4b-d54b-4fdd-b025-c4341e74edd7
(hbnb) all BaseModel
[[BaseModel] (5e21da4b-d54b-4fdd-b025-c4341e74edd7) 
{'id': '5e21da4b-d54b-4fdd-b025-c4341e74edd7',
'created_at': datetime.datetime(2022, 10, 16, 23, 59, 54, 239245),
'updated_at': datetime.datetime(2022, 10, 16, 23, 59, 54, 242660)}]
(hbnb) show BaseModel 5e21da4b-d54b-4fdd-b025-c4341e74edd7
[BaseModel] (5e21da4b-d54b-4fdd-b025-c4341e74edd7)
{'id': '5e21da4b-d54b-4fdd-b025-c4341e74edd7',
'created_at': datetime.datetime(2022, 10, 16, 23, 59, 54, 239245),
'updated_at': datetime.datetime(2022, 10, 16, 23, 59, 54, 242660)}
(hbnb) destroy
** class name missing **
(hbnb) destroy BaseModel
** instance id missing **
(hbnb) destroy BaseModel 5e21da4b-d54b-4fdd-b025-c4341e74edd7
(hbnb) show BaseModel 5e21da4b-d54b-4fdd-b025-c4341e74edd7
** no instance found **
(hbnb) create User
b5e5c1f8-1e14-4a2f-b906-e34450dae0a3
(hbnb) update User b5e5c1f8-1e14-4a2f-b906-e34450dae0a3 name "EDU"
(hbnb) show User b5e5c1f8-1e14-4a2f-b906-e34450dae0a3
[User] (b5e5c1f8-1e14-4a2f-b906-e34450dae0a3)
{'id': 'b5e5c1f8-1e14-4a2f-b906-e34450dae0a3',
'created_at': datetime.datetime(2022, 10, 17, 0, 2, 19, 658539),
'updated_at': datetime.datetime(2022, 10, 17, 0, 2, 46, 435480), 'name': 'EDU'}
(hbnb) update
** class name missing **
(hbnb) update User
** instance id missing **
(hbnb) update User b5e5c1f8-1e14-4a2f-b906-xxxxxxxxxxxxx
** no instance found **
(hbnb) update User b5e5c1f8-1e14-4a2f-b906-e34450dae0a3
** attribute name missing **
(hbnb) update User b5e5c1f8-1e14-4a2f-b906-e34450dae0a3 name
** value missing **
(hbnb) update User b5e5c1f8-1e14-4a2f-b906-e34450dae0a3 name "WILSON"
(hbnb) show User b5e5c1f8-1e14-4a2f-b906-e34450dae0a3
[User] (b5e5c1f8-1e14-4a2f-b906-e34450dae0a3)
{'id': 'b5e5c1f8-1e14-4a2f-b906-e34450dae0a3',
'created_at': datetime.datetime(2022, 10, 17, 0, 2, 19, 658539),
'updated_at': datetime.datetime(2022, 10, 17, 0, 15, 0, 403822), 'name': 'WILSON'}
(hbnb)
(hbnb) quit
root@DESKTOP-F800J0P:~/FullStack-EDU/holbertonschool-AirBnB_clone# echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
(hbnb)
root@DESKTOP-F800J0P:~/FullStack-EDU/holbertonschool-AirBnB_clone#
```
<img src="https://github.com/EduRamos95/holbertonschool-AirBnB_clone/blob/main/img/json1.PNG?raw=true"></img>
<img src="https://github.com/EduRamos95/holbertonschool-AirBnB_clone/blob/main/img/json2.PNG?raw=true"></img>

## Bugs
No known bugs at this time.

## Authors
* Edu Ramos - [Github](https://github.com/EduRamos95)
* Wilson Valer - [Github](https://github.com/WilsonValer)

| [<img src="https://avatars.githubusercontent.com/u/105248833?v=4" width=130><br><sub> Edu Ramos ✒️</sub>](https://github.com/EduRamos95)   | [<img src="https://avatars.githubusercontent.com/u/100174476?v=4" width=130><br><sub> Wilson Valer ✒️</sub>](https://github.com/WilsonValer)  |
|--|--|
|  |  |
|  |  |
