import datetime
class Task:
    
    def __init__(self,title,due_day, comment):
        self.title = title
        self.due_day = due_day
        self.created_day = datetime.datetime.now().date()
        self.comment = comment
        
        print(self.title)
        print(self.due_day)
        print(self.created_day)
        print(self.comment)
        
    
        