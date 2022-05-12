def get_cheapest_hotel(number):   #DO NOT change the function's name
    cheapest_hotel = "cheapest_hotel_name"

    split1 = number.split(':', 1)
    type = split1[0]

    split2 = split1.split(',', -1)
    dates = split2.pop(0)

    for d in dates:
        pass


    return cheapest_hotel
