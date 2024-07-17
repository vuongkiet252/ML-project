from Object.Class import Class
from Object.Teacher import Teacher
from Object.Student import Student


class Output:
	def __init__(self):
		pass

	@staticmethod 
	def menu():
		print("----------------------------")
		print("0. Thoát")
		print("1. Thêm lớp")
		print("2. Thêm giáo viên")
		print("3. Thêm học sinh")
		print("4. Hiển thị thông tin lớp học")
		print("5. Hiển thị thông tin giáo viên")
		print("6. Hiển thị thông tin học sinh")
		print("7. Chỉnh sửa thông tin lớp học")
		print("8. Chỉnh sửa thông tin giáo viên")
		print("9. Chỉnh sửa thông tin học sinh")

class Manage:
	def __init__(self):
		pass

	classes = []
	teachers = []
	students = []

	# CLASS 

	def Check_Class_Exist(self, name, year):
		for index in range (len(self.classes)):
			if name == self.classes[index].name and year == self.classes[index].year:
				return index
		return -1


	def Add_Class(self, name, year):
		index = self.Check_Class_Exist(name, year)
		if index == -1:
			self.classes.append(Class(name, year))
		else:
			print("Class has aldready been created")


	def Get_class_info(self, name, year):
		index = self.Check_Class_Exist(name, year)
		if index != -1:
			print(f"\nTên lớp: {self.classes[index].name}")
			print(f"Niên khóa: {self.classes[index].year}")
			print(f"Số học sinh trong lớp: {len(self.classes[index].lst_student)}")
			print(f"Giáo viên giảng dạy:")
			for i in self.classes[index].lst_teacher:
				print(f"{i.name} môn {i.subject}")
		else:
			print ("Class not found")


	def Modify_Class_Name(self, name, year, new_name): 
		index = self.Check_Class_Exist(name, year)
		if index != -1:
			self.classes[index].name = new_name
		else: 
			print("Class not found")

	def Modify_Class_Year(self, name, year, new_year): 
		index = self.Check_Class_Exist(name, year)
		if index != -1:
			self.classes[index].year = new_year
		else: 
			print("Class not found")

	def Erase_Class(self, name, year):
		index = self.Check_Class_Exist(name, year)
		if index != -1:
			self.classes.pop(self.classes[index])
		else: 
			print("Class not found")

	def Get_available_classes(self, subject) -> list:
		available = []
		for i in self.classes:
			if subject not in i.lst_subject:
				available.append(i)
		return available
	
	# TEACHER

	def Check_Teacher_Exist(self, name, birth, subject):
		for index in range (len(self.teachers)):
			if name == self.teachers[index].name and birth == self.teachers[index].birth and subject == self.teachers[index].subject:
				return index
		return -1


	def Add_Teacher(self, name, birth, subject):
		index = self.Check_Teacher_Exist(name, birth, subject)
		if index == -1:
			self.teachers.append(Teacher(name, birth, subject))
		else:
			print("Teacher has aldready been created")


	def Get_teacher_info(self, name, birth, subject):
		index = self.Check_Teacher_Exist(name, birth, subject)
		if index != -1:
			print(f"\nTên: {self.teachers[index].name}")
			print(f"Bộ môn: {self.teachers[index].subject}")
			print(f"Sinh nhật: {self.teachers[index].birth}")
			print("Giáo viên đang dạy các lớp: ")
			for i in self.teachers[index].lst_clss:
				print(f"{i.name}")
		else:
			print("Teacher not found")

	def Modify_Teacher_Name(self, name, year, subject, new_name): 
		index = self.Check_Teacher_Exist(name, birth, subject)
		if index != -1:
			self.teachers[index].name = new_name
		else: 
			print("Teacher not found")

	def Modify_Teacher_Birth(self, name, year, subject, new_birth):
		index = self.Check_Teacher_Exist(name, birth, subject)
		if index != -1:
			self.teachers[index].birth = new_birth
		else: 
			print("Teacher not found")


	def Modify_Teacher_Subject(self, name, birth, subject, new_subject):
		index = self.Check_Teacher_Exist(name, birth, subject)
		if index != -1:
			for i in self.teachers[index].lst_clss:
				i.lst_subject.remove(self.teachers[index].subject)
			self.teachers[index].subject = new_subject
			for i in self.teachers[index].lst_clss:
				if self.teachers[index].subject in i.lst_subject:
					i.lst_teacher.remove(self.teachers[index])
		else: 
			print("Teacher not found")


	def Choose_class (self, name, birth, subject): # sửa lại
		index = self.Check_Teacher_Exist(name, birth, subject)
		if index != -1:
			available = self.Get_available_classes(self.teachers[index].subject)
			for i in range (len(available)):
				print(f"\n{i}. {available[i].name}")
			new_clss = input("\nVui lòng chọn lớp: ")
			return available[int(new_clss)]
		else:
			print("Teacher not found")


	def Add_teacher_to_class(self, name, birth, subject, clss):
		 index = self.Check_Teacher_Exist(name, birth, subject)
		 if index != -1:
		 	clss.lst_teacher.append(self.teachers[index])
		 	clss.lst_subject.append(self.teachers[index].subject)
		 	self.teachers[index].lst_clss.append(clss)
		 else:
		 	print("Teacher not found")


	def Remove_teacher_from_class(self, name, birth, subject, clss):
		index = self.Check_Teacher_Exist(name, birth, subject)
		if index != -1:
			clss.lst_teacher.remove(self.teachers[index])
			clss.lst_subject.remove(self.teachers[index].subject)
			self.teachers[index].lst_clss.remove(clss)
		else:
			print("Teacher not found")

	def Erase_Teacher(self, name, birth, subject):
		index = self.Check_Teacher_Exist(name, birth, subject)
		if index != -1:
			self.teachers.pop(self.teachers[index])
		else: 
			print("Teacher not found")

	# STUDENT
	def Check_Student_Exist(self, name, birth, name_clss, year_clss):
		for index in range (len(self.students)):
			if name == self.students[index].name and birth == self.students[index].birth and name_clss == self.students[index].clss.name and year_clss == self.students[index].clss.year:
				return index
		return -1

	def Add_Student(self, name, birth, name_clss, year_clss):
		index = self.Check_Student_Exist(name, birth, name_clss, year_clss)
		class_index = self.Check_Class_Exist(name_clss, year_clss)
		if index == -1:
			if class_index != -1:
				self.students.append(Student(name, birth, self.classes[class_index]))
			else:
				print("Class not found")
		else:
			print("Student has aldready been created")


	def Get_student_info(self, name, birth, name_clss, year_clss):
		index = self.Check_Student_Exist(name, birth, name_clss, year_clss)
		if index != -1:
			print(f"\nTên: {self.students[index].name}")
			print(f"Lớp: {self.students[index].clss.name}")
			print(f"Niên khóa: {self.students[index].clss.year}")
			print(f"Sinh nhật: {self.students[index].birth}")

			print(f"Giáo viên giảng dạy: ")
			for i in self.students[index].clss.lst_teacher:
				print(f"{i.name} (môn {i.subject})")


	def Modify_Student_Name(self, name, birth, name_clss, year_clss, new_name):
		index = self.Check_Student_Exist(name, birth, name_clss, year_clss)
		if index != -1:
				self.students[index].option[key] = new_name
		else: 
			print("Student not found")

	def Modify_Student_Birth(self, name, birth, name_clss, year_clss, new_birth):
		index = self.Check_Student_Exist(name, birth, name_clss, year_clss)
		if index != -1:
				self.students[index].birth = new_birth
		else: 
			print("Student not found")

	def Modify_Student_Class(self, name, birth, name_clss, year_clss, new_clss_name, new_clss_year):
		index = self.Check_Student_Exist(name, birth, name_clss, year_clss)
		class_index = self.Check_Class_Exist(new_clss_name, new_clss_year)
		if index != -1:
			if class_index != -1:	
				self.students[index].clss.lst_student.remove(self.students[index])
				self.students[index].clss = self.classes[class_index]
				self.students[index].clss.lst_student.append(self.students[index])
		else:
			print("Student not found")

	def Erase_Student(self, name, birth, new_clss, year_clss):
		index = self.Check_Student_Exist(name, birth, new_clss, year_clss)
		if index != -1:
			self.students.pop(self.students[index])
		else: 
			print("Student not found")