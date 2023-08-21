class railwayForm:
    formtype = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

AhApplication = railwayForm()
AhApplication.name = "Atharv Milind Hingmire"
AhApplication.train = "Rajdhani Express"
AhApplication.printData()

