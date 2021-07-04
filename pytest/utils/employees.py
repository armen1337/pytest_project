class Employee:
	count = 0

	def __init__(self, name: str, age: int):
		self._name = str(name)
		self._age = int(age)
		self._status = "Currently working"
		Employee.count += 1


	@property
	def name(self):
		return self._name


	@property
	def age(self):
		return self._age


	@property
	def status(self):
		return self._status


	def fire(self):
		self._status = "Fired"


	def __del__(self):
		Employee.count -= 1

