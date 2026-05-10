class Student:
    def __init__(self,name,roll_no , marks):
        self.__name = name
        self.__roll_no = roll_no
        self.__marks = marks


    def get_name(self):
        return self.__name

    def get_rollno(self):
        return self.__roll_no

    def get_mark(self):
        return self.__marks

    def set_name(self,name):
        if(name != ""):
          self.__name = name

    def set_roll_no(self,rollno):
        if (rollno>=1 and rollno<=100):
           self.__roll_no = rollno
        else:
            print("invalid rollno")

    def set_marks(self,marks):
        if (marks <=0 ):
            print("invalid")
        else:
           self.__marks=  marks
    def info(self):
        print(f"student name = {self.__name} , {self.__marks} , {self.__roll_no}"
              )

s1 = Student("faa",1010,30)
s1.set_name("fata")
s1.info()
s1.set_marks(70)
s1.info()
print(s1.get_mark())