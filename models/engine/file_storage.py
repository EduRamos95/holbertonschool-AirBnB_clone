#!/usr/bin/python3
"""
Module file_storage
"""


import json
from models.base_model import BaseModel

classes = {"BaseModel": BaseModel}

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
		self.__objects[key_cls] = obj.to_dict()

	def save(self):
		"""Public Method
		serializes __objects to JSON file: __file_path
		"""
		with open(FileStorage.__file_path, 'w') as fd:
			json.dump(FileStorage.__objects, fd)

	def reload(self):
		"""Public Method
		deserializes JSON file: __file_path
		"""
		try:
			with open(FileStorage.__file_path, 'r', encoding="utf-8") as fd:
				json_dict = json.load(fd)
			for key in json_dict.keys():
				FileStorage.__objects[key] = classes[json_dict[key]["__class__"]](**json_dict[key])
		except FileNotFoundError:
			return
				




