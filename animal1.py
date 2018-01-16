class animal(object):
	def __init__(self, name, health):
		self.name = name
		self.health=100
		#attributes: name, health
		#methods: walk, run, display health
	def walk(self):
		self.health-=1
		return self

	def run(self):
		self.health-=5
		return self

	def display_health(self):
		print 'I am '+ self.name
		# print self.health
		print 'I have ' + str(self.health) + ' health'
		return self

class dog(animal):
	def __init__(self, name, health):
		super(dog, self).__init__(name, health)
		self.health=150

	def pet(self):
		self.health+=5
		return self


dog1=dog("dog", 150)
dog1.pet().walk().walk().walk().run().run().display_health()

class dragon(animal):
	def __init__(self, name, health):
		super(dragon, self).__init__(name, health)
		self.health=170

	def fly(self):
		self.health-=10
		return self

dragon1=dragon("dragon", 170)
dragon1.fly().display_health()

class elephant(animal):
	def __init__(self, name, health):
		super(elephant, self).__init__(name, health)
		self.health=160

	def stomp(self):
		self.health-=10
		return self

	def paint(self):
		self.health+=5
		return self

elephant1=elephant("elephant", 160)
elephant1.stomp().paint().display_health()
