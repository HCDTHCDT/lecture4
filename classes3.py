class Flight:
    def __init__(self,origin,destination,duration):
        self.origin=origin
        self.destination=destination
        self.duration=duration
    def print_info(self):
        print("Origin is {}".format(self.origin))    
        print("Destination is {}".format(self.destination))    
        print("Duration is {}".format(self.duration))  

    def delay(self,amount):
        self.duration+=amount

def main():
    f1=Flight(origin="Urmia",destination="Baku",duration=50)
    f1.duration+=10
    f1.print_info()
    f2=Flight("Istanbul","Tehran",50)
    f2.delay(5)
    f2.print_info()

if __name__=="__main__":
    main()        