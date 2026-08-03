"""
name = input("name? ")

if name == "Muhammet" or name == "Ali" or name == "Münevver":
    print("Çınkır")
elif name == "Halil":
    print("Alt")
else:
    print("Who?")
"""


# Burada diğer dillerde olan switch-case yapısının benzerinin aslında pythonda da olduğunu nasıl kullanıldığını gösterdim
# Her şey aynı işlevi görüyor. Bazılarında biraz kısayollar var.


"""
name = input("name? ")

match name:
    case "Muhammmet":
        print("Çınkır")
    case "Ali":
        print("Çınkır")
    case "Münevver":
        print("Çınkır")
    case "Halil":
        print("Alt")
    case _:
        print("Who?")
"""

"""
name = input("name? ")

match name:
    case "Muhammmet" | "Münevver" | "Ali":
        print("Çınkır")
    case "Halil":
        print("Alt")
    case _:
        print("Who?")
"""
