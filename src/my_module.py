class Hotel:
   def __init__(self, name:str, precoSRegular:int, precoSReward:int, precoFSRegular:int, precoFSReward:int, classificacao:int):
        self.name:str = name
        self.pg1:int = precoSRegular
        self.pw1:int = precoSReward
        self.pg2:int = precoFSRegular
        self.pw2:int = precoFSReward
        self.stars:int = classificacao

class stay:
    def __init__(self, hotel:Hotel, tipo:str):
        self.hotel:Hotel = hotel
        self.__ptotal:int = 0
        if tipo == "Regular":
            self.__Ctipo:str = "g"
        elif tipo == "Reward":
            self.__Ctipo:str = "w"

    def set_price(self, day):
        Wdays = ["mon", "tues", "wed", "thur", "fri"]
        WEdays = ["sat", "sun"]
        if day in Wdays and self.__Ctipo == "g":
            self.__ptotal += self.hotel.pg1
        elif day in Wdays and self.__Ctipo == "w":
            self.__ptotal += self.hotel.pw1
        elif day in WEdays and self.__Ctipo == "g":
            self.__ptotal += self.hotel.pg2
        elif day in WEdays and self.__Ctipo == "w":
            self.__ptotal += self.hotel.pw2

    def get_price(self)->int:
        return self.__ptotal




def get_cheapest_hotel(number):   #DO NOT change the function's name   
    Lake = Hotel("Lakewood", 110, 80, 90, 80, 3)
    Brigde = Hotel("Bridgewood", 160, 110, 60, 50, 4)
    Ridge = Hotel("Ridgewood", 220, 100, 150, 40, 5)
    
    split1 = number.split(':', 1)
    type = split1[0]

    split2 = split1.split(',', -1)
    dates = split2.pop(0)

    totalp = 0

    stayL = stay(Lake,type)
    stayB = stay(Brigde,type)
    stayR = stay(Ridge,type)
        
    for d in dates:
        day = d.split('(').pop(0).split(')')[0]
        stayL.set_price(day)
        stayB.set_price(day)
        stayR.set_price(day)


    
