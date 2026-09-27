#Homework: Find the final probability for this sentence "hi can I order pizza"
#5/16


#P(hi|order_pizza) = (2 + 1)/5 + 11
hi = 0.1875
can = 0.125
i = 0.125
order = 0.125
pizza = 0.125
#multiply everything:
def final_probability():
  return hi * can * i * order * pizza
final_probability()
#0.00004577636 is low for greetings, try order_pizza

hi = 1/16
can = 2/16
i = 2/16
order = 2/16
pizza = 2/16
final_probability()
#rounded is 0.0001525878
#
#comparing 0.00004577636 for greeting and 0.0001525878 for order pizza, the percentages would be 20.5% the model predicts the input is a greeting
#and a 79.3% the model decides the input is a pizza order.
#the model would most likely choose order_pizza.
