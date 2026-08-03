"""
def main():
    number = int(input("what is the number? "))
    parity(number)



def parity(number):
    if number % 2 == 1:
        print("The number is odd.")
    else:
        print("The number is even.")

main()
"""

def main():
    number = int(input("number: "))
    if is_even(number):
        print(f"{number} is even")
    else:
        print(f"{number} is odd")


def is_even(n):
    if n % 2 == 0:
        return 1 # bu kısımda 'return True' yazman daha iyi olacak
    else:
        return 0 # bu kısmda 'return False' yazman daha doğru olacak

main()


"""Pythonic Yazım:
if n % 2 == 0:
    return True
else:
    return False

yukarıdaki bu ifade tek bir satırda yazılabilir:
return True if n % 2 == 0 else False
ya da:
return n % 2 == 0
"""





