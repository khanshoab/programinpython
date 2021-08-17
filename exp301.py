# experiment 3.1
# program to implement class ,objects and static method

class student:
    no_of_courses=5
    credits=25

    def setval(self,rollno,name,add,mob):
        self.rollno=rollno
        self.name=name
        self.add=add
        self.mob=mob
    def getval(self):
        print('self is at',id(self))
        return self.rollno,self.name,self.add,self.mob,self.no_of_courses
    @classmethod

    def setcourses(cls,c):
        cls.no_of_courses
    @classmethod

    def setcredits(cls,c):
        cls.credits=c
    @staticmethod

    def is_workday(day):    
        if day.workday()==6:
            return False
        return True    

    def main():
        s=student()
        s.setval('19c033','khan shoab akhtar','vasai',9372514976)
        print(s.getval())
        s.setcourses(7)
        print(s.getval())
        s1=student()
        s1.setval('19co32','khan rehan','jageshvari',98227781297)
        print(s1.getval())
        s1.setcredits(30)
        import daretime
        d=datetime.date(2021,6,19)
        print('is workday?',student.is_workday(d))
    if__name__=='__main__':
       main() 
       