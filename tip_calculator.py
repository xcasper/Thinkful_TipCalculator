def tip_calculator():
    meal_cost = 20
    tax_rate = .15
    tip_rate = .15
    tax_amount = meal_cost * tax_rate
    tip_amount = (meal_cost + tax_amount) * tip_rate
    total = meal_cost + tax_amount + tip_amount

    print "The base cost of your meal was $%.2f" % meal_cost
    print "You need to pay $%.2f for tax" % tax_amount
    print "Tipping at a rate of %.2f%%, you should leave $%.2f for a tip." % ((tip_rate * 100), tip_amount)
    print "The grand total of your meal is $%.2f ." % total

tip_calculator()
