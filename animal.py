class animal(object):
	def __init__(self, name, health):
		self.name = name
		self.health=100
		#attributes: name, health
		#methods: walk, run, display health
	def walk(self):
		self.health=100
		self.name=name

	def run(self):
		self.health-=5
		return self

	def display_health(self):
		print 'I am a(n):'+ self.name
		print 'I have:' + str(self.health) + 'health'
		return self

	# animal=Animal('')

class dog(animal):
	def __init__(self, ):
		super(animal, self).__init__()
		#attr: default health of 150
	def pet(self):
		pass
		return self
	def bark(self):
		pass
		return self
		#metho: pet, bark
class dragon(animal):
	def __init__(self, arg):
		super(animal, self).__init__()
		self.arg = arg
	def fly(self):
		pass
		return self
	def flamethrower(self):
		pass
		return self
		#attr: default health of 170
		#metho:fly, flamethrower, display health
class elephant(animal):
	def __init__(self, arg):
		super(animal, self).__init__()
		self.arg = arg
	def stomp(self):
		pass
		return self
	def paint(self):
		pass
		return self

		#attr: default health of 160
		#metho: stomp, paint, display health

dog1=dog()
dog1.pet().bark()

dragon1=dragon()
dragon1.fly().flamethrower()

elephant1=elephant()
elephant1=stomp().paint()
