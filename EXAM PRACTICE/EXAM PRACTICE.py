Value = int(input("Enter integer (0-99):"))
Operation = str(input("Calculate the multiplicative or additive persitant (A or M)?"))

count = 0
while Value > 9:
    if Value != 9:
        print("Error retry")
    count = count + 1
    if Operation == "A" or Operation == "a":
        Value = (Value / 10) + (Value % 10)
        print("The persistence is",Value)
    elif Operation == "M" or Operation == "m":
        Value = (Value/ 10) * (Value % 10)
        print("The persistence is:",Value)