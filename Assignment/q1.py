usd_amount = float(input("Enter amount sent in USD: "))
exchange_rate = float(input("Enter current exchange rate (1 USD in NPR): "))
fee_percentage = float(input("Enter service fee percentage: "))

npr_amount = usd_amount * exchange_rate

fee = (npr_amount * fee_percentage) / 100

final_amount = npr_amount - fee

print(f"Converted Amount: NPR {npr_amount:.2f}")
print(f"Service Fee: NPR {fee:.2f}")
print(f"Final Amount Received: NPR {final_amount:.2f}")

