from Object.Class import Class
from Object.Teacher import Teacher
from Object.Student import Student
from Manipulator import Output, Manage


# print("----------------------------")
	#	print("0. Thoát")
	#	print("1. Thêm lớp")
	#	print("2. Thêm giáo viên")
	#	print("3. Thêm học sinh")
	#	print("4. Hiển thị thông tin lớp học")
	#	print("5. Hiển thị thông tin giáo viên")
	#	print("6. Hiển thị thông tin học sinh")
	#	print("7. Chỉnh sửa thông tin lớp học")
	#	print("8. Chỉnh sửa thông tin giáo viên")
	#	print("9. Chỉnh sửa thông tin học sinh")

Output.menu()
while True:
	option_index = input("Vui lòng chọn lệnh: ")
	access = Manage()
	if option_index == "0":
		break
	if option_index == "1":
		class_name = input("Nhập tên lớp: ")
		class_year = input("Nhập niên khóa: ")
		access.Add_Class(class_name, class_year)
	if option_index == "2":
		teacher_name = input("Nhập tên giáo viên: ")
		teacher_birth = input("Nhập ngày sinh: ")
		teacher_subject = input("Nhập môn dạy: ")
		access.Add_Teacher(teacher_name, teacher_birth, teacher_subject)
	if option_index == "3":
		student_name = input("Nhập tên học sinh: ")
		student_birth = input("Nhập ngày sinh: ")
		student_class_name = input("Nhập lớp: ")
		student_class_year = input("Niên khóa: ")
		access.Add_Student(student_name, student_birth, student_class_name, student_class_year)
	if option_index == "4":
		print("Bạn muốn hiển thị thông tin cho lớp nào?")
		class_name = input("Nhập tên lớp: ")
		class_year = input("Nhập niên khóa: ")
		access.Get_class_info(class_name, class_year)
	if option_index == "5":
		print("Bạn muốn hiển thị thông tin cho giáo viên nào?")
		teacher_name = input("Nhập tên giáo viên: ")
		teacher_birth = input("Nhập ngày sinh: ")
		teacher_subject = input("Nhập môn dạy: ")
		access.Get_teacher_info(teacher_name, teacher_birth, teacher_subject)
	if option_index == "6":
		print("Bạn muốn hiển thị thông tin cho học sinh nào?")
		student_name = input("Nhập tên học sinh: ")
		student_birth = input("Nhập ngày sinh: ")
		student_class =	input("Nhập lớp: ")
		access.Get_student_info(student_name, student_birth, student_class)
	if option_index == "7":
		print("Bạn muốn chỉnh sửa thông tin lớp nào?")
		class_name = input("Nhập tên lớp: ")
		class_year = input("Nhập niên khóa: ")
		print("1. Tên")
		print("2. Niên khóa")
		print("3. Xóa lớp")
		print("Bạn muốn chỉnh sửa thông tin nào của lớp?")
		option = input()
		if option == "1": 	
			new_name = input("Vui lòng nhập tên lớp mới: ") 
			access.Modify_Class_Name(class_name, class_year, new_name)
		if option == "2":
			new_year = input("Vui lòng nhập niên khóa mới: ")
			access.Modify_Class_Year(class_name, class_year, new_year)
		if option == "3":
			access.Erase_Class(class_name, class_year) 
	if option_index == "8":
		print("Bạn muốn chỉnh sửa thông tin giáo viên nào?")
		teacher_name = input("Nhập tên giáo viên: ")
		teacher_birth = input("Nhập ngày sinh: ")
		teacher_subject = input("Nhập môn dạy: ")
		print("1. Tên")
		print("2. Ngày sinh")
		print("3. Môn dạy")
		print("4. Thêm lớp dạy")
		print("5. Bỏ lớp dạy")
		print("6. Xóa giáo viên")
		if option == "1":
			new_name = input("Vui lòng nhập tên giáo viên mới: ") 
			access.Modify_Teacher_Name(teacher_name, teacher_birth, teacher_subject, new_name)
		if option == "2":
			new_birth = input("Vui lòng nhập ngày sinh mới: ")
			access.Modify_Teacher_Birth(teacher_name, teacher_birth, teacher_subject, new_birth)
		if option == "3":
			new_subject = input("Vui lòng nhập môn dạy mới: ")
			access.Modify_Teacher_Subject(teacher_name, teacher_birth, teacher_subject, new_subject)
		if option == "4":
			new_class = access.Choose_class(teacher_name, teacher_birth, teacher_subject)
			access.Add_teacher_to_class(teacher_name, teacher_birth, teacher_subject, new_class)
		if option == "5":
			remove_class = input("Vui lòng nhập lớp cần bỏ: ")
			access.Remove_teacher_from_class(teacher_name, teacher_birth, teacher_subject, remove_class)
		if option == "6":
			access.Erase_Teacher(teacher_name, teacher_birth, teacher_subject)
	if option_index == "9":
		print("Bạn muốn chỉnh sửa thông tin học sinh nào?")
		student_name = input("Nhập tên học sinh: ")
		student_birth = input("Nhập ngày sinh: ")
		student_class_name = input("Nhập tên lớp hiện tại: ")
		student_class_year = input("Nhập niên khóa: ")
		print("1. Tên")
		print("2. Ngày sinh")
		print("3. Lớp")
		print("4. Xóa học sinh")
		if option == "1":
			new_name = input("Vui lòng nhập tên học sinh mới: ") 
			access.Modify_Student_Name(student_name, student_birth, student_class_name, student_class_year, new_name)
		if option == "2":
			new_birth = input("Vui lòng nhập ngày sinh mới: ")
			access.Modify_Student_Birth(student_name, student_birth, student_class_name, student_class_year, new_birth)
		if option == "3":
			new_class_name = input("Vui lòng nhập tên lớp mới: ")
			new_class_year = input("Vui lòng nhập niên khóa mới:")
			access.Modify_Student_Class(student_name, student_birth, student_class_name, student_class_year, new_class_name, new_class_year)
		if option == "4":
			access.Erase_Student(student_name, student_birth, student_class_name, student_class_year)
else:
	print("Invalid command")
