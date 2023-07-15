class Soldier:
    def __init__(self, first_name, last_name , birth):
        self.first_name = first_name
        self.last_name = last_name
        self.birth = birth
    
    def __del__(self):
        print( "Soldier", self.first_name, self.last_name , "killed in action")


p1 = Soldier("Lukaz", "Chenco" , "2002-10-01")
print("- First name:" , p1.first_name)
print("- Last name:" , p1.last_name)
print("- Birthday:" , p1.birth)



del Soldier

