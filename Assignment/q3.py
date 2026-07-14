trekkers = int(input("Enter number of trekkers: "))
tims_fee = float(input("Enter TIMS card fee per person: "))
acap_fee = float(input("Enter ACAP permit fee per person: "))

cost_per_person = tims_fee + acap_fee

total_cost = trekkers * cost_per_person

service_charge = (total_cost * 5) / 100

final_cost = total_cost + service_charge

average_cost = final_cost / trekkers

print(f"Total Trek Cost: Rs. {final_cost:.2f}")
print(f"Average Cost per Person: Rs. {average_cost:.2f}")