class Human():
	'''인간'''
	def create(name,weight):
		person = Human()
		person.name = name
		person.weight = weight
		return person

	def eat(person):
		person.weight += 0.1
		print("{}가 먹어서 {}kg이 되었습니다.".format(person.name,person.weight))
		
	def walk(person):
		person.weight -= 0.1
		print("{}가 걸어서 {}kg이 되었습니다.".format(person.name, person.weight))
	
#Human.create = create_human
#Human.eat = eat
#Human.walk =walk

person = Human.create("철수",60.5)
person.walk()
person.eat()
person.walk()