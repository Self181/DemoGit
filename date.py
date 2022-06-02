from datetime import date,datetime
date = date.today()
time = datetime.now()
currenttime = time.strftime('%H:%M:%S')
print(str(date),str(currenttime))


class mobile:
    def __init__(self,name,model):
        self.model = model
        self.name = name
        print(self.name, self.model)

mob1 = mobile('Samsung','S11')
mob2 = mobile('Moto','e4 plus')








