class Flight:
    def __init__(self,origin,destination,duration):
        self.origin=origin
        self.destination=destination
        self.duration=duration

def main():
    f=Flight(origin="Urmia",destination="Baku",duration=50)
    f.duration+=10
    print(f.destination)
    print(f.origin)
    print(f.duration) 
if __name__=="__main__":
    main()        