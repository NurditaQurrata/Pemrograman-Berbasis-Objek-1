

class India(): 
	def capital(self): 
		print("New Delhi adalah ibukota India.") 

	def language(self): 
		print("Hindi adalah bahasa utama India.") 

	def type(self): 
		print("India adalah negara berkembang.") 

class USA(): 
	def capital(self): 
		print("Washington, D.C. adalah ibukota USA.") 

	def language(self): 
		print("English adalah bahasa utama USA.") 

	def type(self): 
		print("USA adalah negara maju.") 

obj_ind = India() 
obj_usa = USA() 
for country in (obj_ind, obj_usa): 
	country.capital() 
	country.language() 
	country.type() 


