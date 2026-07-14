previous = float(input("Enter previous meter reading (kWh): "))
current = float(input("Enter current meter reading (kWh): "))

rate_per_unit = 12.50
service_charge = 75.00

units_consumed = current - previous

energy_charge = units_consumed * rate_per_unit
total_bill = energy_charge + service_charge

print(f"Units Consumed: {units_consumed:.2f} kWh")
print(f"Energy Charge: Rs. {energy_charge:.2f}")
print(f"Service Charge: Rs. {service_charge:.2f}")
print(f"Total Bill: Rs. {total_bill:.2f}")