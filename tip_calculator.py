def tip_calculator():
    meal_cost = int(raw_input("How much did the meal cost before tax? "))
    tax_rate = int(raw_input("How much was the tax rate? ")) / 100.00
    tip_rate = int(raw_input("How percentage would you like to tip? ")) / 100.00
    tax_amount = meal_cost * tax_rate
    tip_amount = (meal_cost + tax_amount) * tip_rate
    total = meal_cost + tax_amount + tip_amount

    print "The base cost of your meal was $%.2f" % meal_cost
    print "You need to pay $%.2f for tax" % tax_amount
    print "Tipping at a rate of %.2f%%, you should leave $%.2f for a tip." % ((tip_rate * 100), tip_amount)
    print "The grand total of your meal is $%.2f ." % total


tip_calculator()
