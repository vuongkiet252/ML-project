

class Student():
	def __init__ (self, name, birth, clss):		
		self.name = name
		self.birth = birth
		self.clss = clss
		self.clss.lst_student.append(self)