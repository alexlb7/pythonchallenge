class Hotel:
   def __init__(self, name:str, precoSRegular:int, precoSReward:int, 
                precoFSRegular:int, precoFSReward:int, classificacao:int):
        self.name:str = name
        self.pg1:int = precoSRegular
        self.pw1:int = precoSReward
        self.pg2:int = precoFSRegular
        self.pw2:int = precoFSReward
        self.stars:int = classificacao

class stay:
    def __init__(self, hotell:Hotel):
        self.hotel:Hotel = hotell
        self.__ptotal:int = 0

    def set_price(self, day:str, tipo:str):
        Wdays = ['mon', 'tues', 'wed', 'thur', 'fri']
        WEdays = ['sat', 'sun']
        if day in Wdays and tipo == "Regular":
            self.__ptotal += self.hotel.pg1
        elif day in Wdays and tipo == "Reward":
            self.__ptotal += self.hotel.pw1
        elif day in WEdays and tipo == "Regular":
            self.__ptotal += self.hotel.pg2
        elif day in WEdays and tipo == "Reward":
            self.__ptotal += self.hotel.pw2 

    def get_price(self)->int:
        return self.__ptotal

def get_cheapest_hotel(number):   #DO NOT change the function's name   

    Lake = Hotel("Lakewood", 110, 80, 90, 80, 3)
    Brigde = Hotel("Bridgewood", 160, 110, 60, 50, 4)
    Ridge = Hotel("Ridgewood", 220, 100, 150, 40, 5)
    stayL = stay(Lake)
    stayB = stay(Brigde)
    stayR = stay(Ridge)  
     
    split = number.split(':', 1)
    type = split[0]
    dates = split[1].split(',')

    for d in dates:
        day = d[ d.find("(") + len("(") : d.find(")") ]

        stayL.set_price(day,type)
        stayB.set_price(day,type)
        stayR.set_price(day,type)

    stays = [stayL,stayB,stayR]
    stays.sort(key= lambda x: (x.get_price(), -x.hotel.stars))
    return stays[0].hotel.name
