def getinfo_class(a): 
		print(f"Lop: {a.name}")
		print(f"Nien khoa: {a.year}")
		print(f"Lop: {a.name} dang co {a.number_student} hoc sinh")
		print("Giao vien:")

		if len(a.gv_lst) == 0:
			print("Khong co")

		for gv in a.gv_lst:
			print(f"{gv.name} day mon {gv.subject}")

		print("------------------------------------")

def getinfo_teacher(a):
		print(f"Ten: {a.name}")
		print(f"Bo mon: {a.subject}")
		print(f"Sinh nhat: {a.birth}")
		print("Giao vien day lop: ")

		if len(a.lop_lst) == 0:
			print("Khong co")

		for lop in a.lop_lst:
			print(f"{lop.name}")

		print("------------------------------------")

def getinfo_student(a): 
		print(f"Ten: {a.name}")
		print(f"Sinh nhat: {a.birth}")
		print(f"Hoc sinh hoc lop: {a.Cls.name}")
		print(f"Nien khoa: {a.Cls.year}")

		for gv in a.Cls.gv_lst:
			print(f"{gv.name} day mon {gv.subject}")

		print("------------------------------------")