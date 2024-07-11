class Cls:
	def __init__(self, name, year):
		self.name = name
		self.year = year 
		self.number_student = 0
		self.gv_lst = []

	def getinfo(self):
		print(f"Lop {self.name}")
		print(f"Nien khoa {self.year}")
		print(f"Lop {self.name} dang co {self.number_student} hoc sinh")
		print("Giao vien:")
		for gv in self.gv_lst:
			print(f"{gv.name} day mon {gv.subject}")

	def alterinfo(self, name, year): #sửa lại nên thay = thuộc tính mới
		self.name = name
		self.year = year

	def deleteteacher(self,teacher):
		self.gv_lst.remove(teacher)
		teacher.lop_lst.remove(self)

class Teacher:	
	def __init__(self, name, subject, birth):
		self.name = name
		self.subject = subject
		self.birth = birth
		self.lop_lst = []
	
	def add_loplstandgv_lst(self, clss):
		clss.gv_lst.append(self)
		self.lop_lst.append(clss)

	def getinfo(self):
		print(f"Ten {self.name}")
		print(f"Bo mon {self.subject}")
		print(f"Sinh nhat {self.birth}")
		print("Giao vien day lop: ")
		for lop in self.lop_lst:
			print(f"{lop.name}")

	def alterinfo(self, name, subject, birth):
		self.name = name
		self.subject = subject
		self.birth = birth

class Student:
	def __init__(self, name, Cls, birth):
		self.name = name
		self.birth = birth
		self.Cls = Cls
		self.Cls.number_student += 1

	def getinfo (self):
		print(f"Ten {self.name}")
		print(f"Lop {self.Cls}")
		print(f"Sinh nhat {self.birth}")
		print(f"Hoc sinh hoc lop {self.Cls.name} nien khoa {self.Cls.year}")
		for gv in self.Cls.gv_lst:
			print(f"{gv.name} day mon {gv.subject}")

	def alterinfo(self, name, birth):
		self.name = name
		self.birth = birth
	def changeclass(self, Cls): 
		self.Cls.number_student -= 1
		self.Cls = Cls
		Cls.number_student += 1


Tin1 = Cls("Tin1", 2326)
Tin2 = Cls("Tin2", 2326)

Hai = Teacher("Hai", "Tin", "9/7/1991")
Hai.add_loplstandgv_lst(Tin2)
Hai.add_loplstandgv_lst(Tin1)

Bao = Student("Bao", Tin1, "21_2_2008")
Thu = Student("Thu", Tin1, "5_4_2008")

Tin1.getinfo()
Hai.getinfo()

Bao.alterinfo("Bao","24/2/2008")
Bao.changeclass(Tin2)

Tin1.getinfo()