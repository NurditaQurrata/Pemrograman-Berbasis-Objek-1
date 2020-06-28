##Dalam kasus paling sederhana, fungsi super dapat digunakan untuk mengganti panggilan eksplisit ke Parent .__ init __ (mandiri).
##Contoh intro kami dari bagian pertama dapat ditulis ulang dengan super seperti yang terlihat di bawah ini.
##Perhatikan, bahwa blok kode di bawah ini ditulis dalam Python 3, versi sebelumnya menggunakan sintaks yang sedikit berbeda.
##Selain itu, output telah dihilangkan karena identik dengan blok kode pertama.

# Base or Super class 
class Person(object): 
	def __init__(self, name): 
		self.name = name 
		
	def getName(self): 
		return self.name 
	
	def isEmployee(self): 
		return False

# Inherited or Subclass (Note Person in bracket) 
class Employee(Person): 
	def __init__(self, name, eid): 
		super(Employee, self).__init__(name) 
		self.empID = eid 
		
	def isEmployee(self): 
		return True
		
	def getID(self): 
		return self.empID 

# Driver code 
emp = Employee("Ika", "PT.Yamaha") 
print(emp.getName(), emp.isEmployee(), emp.getID()) 

