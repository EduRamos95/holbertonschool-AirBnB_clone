#!/usr/bin/python3
"""
Module file_storage
"""


import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review



classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}

class FileStorage():
	"""serializes instances to a JSON file
	and deserializes JSON file to instances
	"""

	__file_path = "file.json"
	__objects = {}

	def all(self):
		"""Public Method
		returns the dictionary of objects
		"""
		return (FileStorage.__objects)

	def new(self, obj):
		"""Public Method
		set in __objects with key
		"""
		key_cls = "{}.{}".format(obj.__class__.__name__,obj.id)
		self.__objects[key_cls] = obj

	def save(self):
		"""Public Method
		serializes __objects to JSON file: __file_path
		"""
		json_objects = {}
		for key in FileStorage.__objects:
			json_objects[key] = FileStorage.__objects[key].to_dict()
		with open(FileStorage.__file_path, 'w') as fd:
			json.dump(json_objects, fd)

	def reload(self):
		"""Public Method
		deserializes JSON file: __file_path
		"""
		try:
			with open(FileStorage.__file_path, 'r') as fd:
				json_dict = json.load(fd)
			for key in json_dict.keys():
				class_obj = json_dict[key]["__class__"]
				re_obj = classes[class_obj](**json_dict[key])
				FileStorage.__objects[key] = re_obj
		except FileNotFoundError:
			return
