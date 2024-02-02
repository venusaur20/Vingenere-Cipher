CHARACTER = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10, "k":11, "l":12, "m":13, "n":14, "o":15, "p":16, "q":17, "r":18, "s":19, "t":20, "u":21, "v":22, "w":23, "x":24, "y":25, "z":26, "A":27, "B":28, "C":29, "D":30, "E":31, "F":32, "G":33, "H":34, "I":35, "J":36, "K":37, "L":38, "M":39, "N":40, "O":41, "P":42, "Q":43, "R":44, "S":45, "T":46, "U":47, "V":48, "W":49, "X":50, "Y":51, "Z":52, "1":53, "2":54, "3":55, "4":56, "5":57, "6":58, "7":59, "8":60, "9": 61, "0":62, "`": 92, "~": 64, "!": 65, "@": 67, "#": 68, "$": 69, "%": 70, "^": 71, "^": 72, "&": 73, "*": 74, "(": 75, ")": 76, "-": 77, "_": 78, "=": 79, "+": 80, "[": 81, "{": 82, "]": 83, "}": 84, ";": 85, ":": 86, ",": 87, "<": 88, ".": 89, ">": 90, "/": 91, "?":92, " ":0}


def crypt():
    message_values = []
    for letter in range(len(message)):
        message_values.append(CHARACTER[message[letter]])

    return message_values

def mix(message_values,shift):
    mixed_values = []
    mixed_message = []

    for letter in range(len(message_values)):
        shift.append(shift[letter])
        if len(shift) > len(message_values):
            break

    print(shift)
    for letter in range(len(message_values)):
        mixed_values.append((shift[letter])+(message_values[letter]))
    print(mixed_values)

    for letter in range(len(mixed_values)):
        
        if (mixed_values[letter]) >= (len(CHARACTER)+2):
            mixed_values[letter] -= (len(CHARACTER)+2)

        if (mixed_values[letter]) < 0:
            mixed_values[letter] += (len(CHARACTER)+2)

        print(mixed_values)
        print(len(list(CHARACTER)))
        mixed_message.append(list(CHARACTER.keys())[mixed_values[letter]-1])

    return(''.join(mixed_message))


def tool():
    shift = []
    key = list(input("What is your key? "))

    if mode == "decrypt":
        for letter in range(len(key)):
            shift.append((CHARACTER[key[letter]]-1)*(-1))

    else:
        for letter in range(len(key)):
            shift.append(CHARACTER[key[letter]]-1)

    for value in range(len(shift)):
        
        if shift[value] < 0:
            shift[value] += (len(CHARACTER)+2) 

        elif shift[value] >= (len(CHARACTER)+2):
            shift[value] -= (len(CHARACTER)+2)

        else:
            break

    message_values = crypt()
    print(mix(message_values,shift))    



#---------------Runs-Code-------------------------------------
while True:
    
    while True:
        mode_choice = input("Decrypt or Encrypt? ").upper()

        if "N" in mode_choice:
            mode = ("encrypt")
            break
        elif "D" in mode_choice:
            mode = ("decrypt")
            break
        else:
            print("That wasn't clear. Please try retyping. \n ")
    
    message = list(input(f"What would you like to {mode}? "))

    tool()
    again = input("\nAgain? ").upper()
    if "Y" in again:
        continue
    else:
        break