runes = ['A', "E", "L", "K", "O", "U", "I", "M", "N", "R", "S", "T"]
word = []

for i in range(12):   
    letter = input("Enter the letter: ").upper()

    if letter not in runes:
        print("Invalid letter")
        break

    if letter in ['L', 'U', 'M', 'O', 'S']:   
        word.append(letter)
    

    if len(word) == 5:
        formed_word = ''.join(word)
        if formed_word == "LUMOS":
            print(formed_word, "formed!")
            break
        else:
            print("-1")
