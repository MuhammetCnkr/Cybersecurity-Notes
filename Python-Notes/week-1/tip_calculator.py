"""
def tip(cost, percentage_tip):
    result = float(cost*percentage_tip/100)
    return result

def main():
    cost = float(input("The cost of meal: "))
    percentage_tip = float(input("Percantage : "))
    result = tip(cost,percentage_tip)
    print("Leave ",result,"$",sep="")

main()
"""


def main():
    dollars = dollars_to_float(input("How much? "))
    percent = percent_to_float(input("What percentage? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d): # input   $50.21
    redundant, float_dollars = d.strip().split("$")
    return float(float_dollars)

def percent_to_float(p): # input    15%
    float_percent, redundant = p.strip().split("%")
    return float(float_percent) / 100

main()
