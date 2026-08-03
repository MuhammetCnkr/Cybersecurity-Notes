def main():
    calculation = input("What do you wanna calculate? ")
    n1, operation, n2 = calculation.strip().split(" ")
    n1, n2 = float(n1), float(n2)
    print(answer(n1,operation,n2))


def answer(n1,operation,n2):

    match operation:
        case "+":
            return n1 + n2
        case "-":
            return n1 - n2
        case "*":
            return n1 * n2
        case "/":
             return n1 / n2
        case "%":
             return n1 % n2
        case _:
            return "Hatalı işlem"

main()

