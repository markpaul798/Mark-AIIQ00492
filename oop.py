class Student:
     def__init____(self,name,estates,course);
      if not name:
        raise ValueError("please provide name")
          self.name=name
          self.estates=estates
          self.course=course

          def__str__(self);
                return f"{self.name}is from{self.estates}and is doing{self.course}"
     
        #Getter for the estate
        @ property
        def estates(self):
           return self._estates

        #Setter for the estate
        @estates.setter
        def estates(self,estates )
           
      def main():
        student =get_student()
        print(student)


        def get_student():
           name=input("what is your name?").strip()
           estates=input("which estates do you come from?").strip()
           course=input("which do you do?").strip()
           return Student(name,estates,course)

           if __name__=="__main__":
              main()