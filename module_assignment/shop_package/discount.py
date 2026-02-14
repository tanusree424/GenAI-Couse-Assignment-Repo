def apply_discount(price, percent):
    discounted_price =  price - (percent/100 *price)
    return discounted_price
def flat_discount(price):
    return price - 50