def percents (x,y):
    """What percents x"""
    one_percent = x / 100
    result = y / one_percent
    print(str(y) + " is " + str(result) + " percent of " + str(x) )
percents(200,50)