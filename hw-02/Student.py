# The Student class (you'll edit and expand on this)
class Student():
    '''
    This class is designed to include information about individual students.
    Currently this class has the following attributes:
    
    name : this is the student's name
    gpa : this is the student's curret gpa
    '''
    
    def __init__(self, name='', gpa=0.0, year=0.0, enroll=['CMSE 202', 'ISP 205', 'HB 409']):
        self.name = name
        self.gpa = gpa
        self.year = year
        self.enroll = enroll
        
    def get_name(self):
        '''
        This function prints the name of the student
        '''
        print("My name is", self.name)
        return
        
    def display_courses(self):
        '''
        This function prints the courses the student is taking
        '''
        print("I am enrolled in:", self.enroll)
        return
        
    def years_until_graduation(self):
        '''
        This function prints the number of years left until the student graduates
        '''
        return 4-self.year
    
class Spartan():
    
    def __init__(self,name):        
        Student.__init__(self,name)
        self.name = name
                
    def set_motto(self, motto):
        
        self.motto = motto
        
        return
    
    def school_spirit(self):
        
        print('My name is', self.name)
        print('I am a Spartan. My motto is', self.motto) 
        
        return
        