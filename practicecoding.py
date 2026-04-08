minutes = input("Enter the total minutes: ")
texts = input("Enter the total texts: ")

total_minutes = 0.10 * int(minutes)
total_texts = 0.05 * int(texts)
montly_charge = 10.00

total_cost = total_minutes + total_texts + montly_charge
print(total_cost)