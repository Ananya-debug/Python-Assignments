#Write a discount coupon code using dictionary in Python with different rate coupons for each day of the week.

discount_coupons = {
     'MONDAY' : '10% OFF',
     'TUESDAY' : '15% OFF',
     'WEDNESDAY' : '20% OFF',
     'THURSDAY' : '25% OFF',
     'FRIDAY' : '30% OFF',
     'SATURDAY' : '35% OFF',
     'SUNDAY' : '40% OFF'
}

day = input("Enter a day of the week : ").upper()

if day in discount_coupons :
     print("Discount coupon of ",day," : ",discount_coupons[day])
else:
     print("Invalid Input")