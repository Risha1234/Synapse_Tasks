runes = ['A', "E", "L", "K", "O", "U", "I", "M", "N", "R", "S", "T"]
word = []
attempts = 0  #counts only valid attempts

while attempts < 12:
    letter = input("Enter the letter: ").upper()

    if letter not in runes:
        print("Invalid letter")
        continue  #invalid letters do not count toward attempts

    attempts += 1  #increment only for valid letters

 
    if letter in ['L', 'U', 'M', 'O', 'S'] and letter not in word:   
        word.append(letter)


    if set(word) == set(['L', 'U', 'M', 'O', 'S']):
        print("LUMOS formed!")
        break  


if set(word) != set(['L', 'U', 'M', 'O', 'S']):
    print("-1")
