# Paru Maharjan
# Online Store Discount System 

purchase = float(input("Enter the total purchase amount (NPR): "))
member = input("Are you a loyalty member? (yes/no): ")

if purchase < 1000:
    discount = 0
elif purchase < 5000:
    discount = 5
elif purchase < 15000:
    discount = 10
else:
    discount = 20

discounted_amount = purchase - (purchase * discount / 100)

if member.lower() == "yes":
    discounted_amount = discounted_amount - (discounted_amount * 5 / 100)

total_discount = purchase - discounted_amount

print(f"Original Amount: NPR {purchase:.2f}")
print(f"Total Discount: NPR {total_discount:.2f}")
print(f"Final Payable Amount: NPR {discounted_amount:.2f}")