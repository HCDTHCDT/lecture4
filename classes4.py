class Flight:
    counter=1
    def __init__(self,origin,destination,duration):
        self.id=Flight.counter
        Flight.counter+=1

        self.passengers=[]

        self.origin=origin
        self.destination=destination
        self.duration=duration
    def print_info(self):
        print("Origin is {}".format(self.origin))    
        print("Destination is {}".format(self.destination))    
        print("Duration is {}".format(self.duration)) 
        print("Passengers:")
        for passenger in self.passengers:
            print("{}".format(passenger.name))    

    def delay(self,amount):
        self.duration+=amount
    def add_passenger(self,p):
        self.passengers.append(p)
        p.flight_id=self.id

class Passenger():
    def __init__(self,name):
        self.name=name


def main():
    f1=Flight(origin="Urmia",destination="Baku",duration=50)
    kaki=Passenger("Kaki")
    hasi=Passenger("Hasi")
    f1.add_passenger(kaki)
    f1.add_passenger(hasi)
    f1.print_info()
    print(kaki.flight_id)
    #vip
    
if __name__=="__main__":
    main()        