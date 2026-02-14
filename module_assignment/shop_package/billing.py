def calculate_total(prices):
   total =0
   for p in prices:
    total += p
   return total
def apply_tax(price):
    return price + (price*5/100)