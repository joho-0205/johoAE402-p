class People():
    def setdata(self,name,gender,age,hair,weight):
        self.name = name
        self.gender = gender
        self.age = age
        self.hair = hair
        self.weight = weight
    def showdata(self):
        print("Name:",self.name,"\nGender:",self.gender,"\nAge:",self.age,"\nHair Color:",self.hair,"\nWeight",self.weight)
a = People()
name = input("What's your name?")
gender = input("What's your gender?")
age = input("How old are you?")
hair = input("What's your hair color?")
weight = input("What's your weight?")
a.setdata(name,gender,age,hair,weight)
print(a.showdata())
