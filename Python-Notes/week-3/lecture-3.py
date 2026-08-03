#WHILE:

i = 3
while i != 0:
    print("meow")
    i -= 1 # i = i -1   # aslında burada asignmentın güzel bir örneği var

#FOR:


for i in [0,1,2]:
    print("meow")


for i in range(3):
    print("meow")


for _ in range(3): #Pythonic bir yöntem
    print("meow")


print("meow\n" * 3) #Bu en alta bir tane ekstra bir satır ekler
print("meow\n" * 3, end="") #Bu en altta fazladan satırı eklemeyi engeller



while True:
    n = int(input("What is n? "))
    if n < 0:
        continue
    else:
        break


while True:
    n = int(input("What is n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")




def main():
    number = get_number()
    meow(number)

def meow(n):
    for _ in range(n):
        print("meow")

def get_number():
    while True:
        number = int(input("Number? "))
        if number > 0:
            return number # burada break kullanırsan main fonksiyonda number'a return value yapamazsın yapman için aşağıdaki yerde return yapman lazım
        #return number



#LIST


students = ["muhammet","ali","münevver"]

print(students[0]) #zero indeksi yazdırır

for i in range(3):
    print(students[i]) #0. 1. 2. indeksteki verileri yazar

for student in students:
    print(student) # student stundestaki verileri alıp ekrana yazılır


#LEN

len(students) #listenin uzunluğunu verir

for i in range(len(students)):
    print(i, students[i])

#DICT : Keys and Values


names = {
    "Muhammet":"Çınkır",
    "Ali":"Çınkır",
    "Halil":"Alt"
}

print(names["Muhammet"]) #Çınkır yazar


for name in names:
    print(name) #Bu sadece keyleri basar ekrana

for name in names:
    print(name, names[student], sep=", ") #Bu kısımda ilk önce key kısmı bastı ardından key indeksli value kısmını bastı ekrana


students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
] # None boş bırakmak için kullanılır
# Yukarıda her bir dictin 3 tane keyi ve 3 tane valuesu var ve bu dictler bir listede indeksli şekilde sıralılar.


for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")



def main():
    print_square(3)


def print_square(size):

    # For each row in square
    for i in range(size):

        # For each brick in row
        for j in range(size):

            #  Print brick
            print("#", end="")

        # Print blank line
        print()


main()
