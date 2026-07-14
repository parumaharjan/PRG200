salary = float(input("Enter monthly basic salary: "))
deduction_rate = 10 

bonus = salary

deduction = (bonus * deduction_rate) / 100

take_home_bonus = bonus - deduction

print(f"Dashain Bonus: Rs. {bonus:.2f}")
print(f"Deduction: Rs. {deduction:.2f}")
print(f"Final Take-home Bonus: Rs. {take_home_bonus:.2f}")


