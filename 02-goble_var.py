#函数的定义以及全局局部变量的使用
get_name = input("please input name:")
get_age = int(input("please input age:"))
def print_base_info():
	global get_age
	get_age = 10
	print("the one name is %s age %d"%(get_name,get_age))

def print_old_inf():
	get_age = 10
	print("the second name is %s age %d"%(get_name,get_age))
print_base_info()
print_old_inf()

print("---hello---!!")