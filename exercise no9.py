#tip calculator
name=input('Please enter your name:')
print('Welcome to Grand Cafe', name)
meal_bill=eval(input('Enter the price of the ordered meal:'))
tip_percentage=eval(input('Enter the tip percenatage(e.g 15 for 15%)'))
tip_amnt=(meal_bill * tip_percentage)/100
total_bill=sum([meal_bill,tip_amnt])
print('The tip amount is:', tip_amnt)
print('The total bill is:', total_bill)