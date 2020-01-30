class person:
    
    totalObjects=0
    def __init__(self):
        person.totalObjects=person.totalObjects+1

    #@classmethod
    def showcount(self):
        print("Total objects: ",self.totalObjects)

obj1=person()

person.showcount()


class greeting:
    @staticmethod
    def greet():
        print("Hello!")
'''
