from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceaser(direction, text, shift):
    new_word = ""
    if direction == "encode":
        for letter in text:
            if letter in alphabet:
                index = alphabet.index(letter) + shift
                while index > 26:
                    index -= 26
                letter = alphabet[index]
                new_word += letter
            else:
                new_word += letter
        print(new_word)
    elif direction == "decode":
        for letter in text:
            if letter in alphabet:
                index = alphabet.index(letter) - shift
                while index < 0:
                    index += 26
                letter = alphabet[index]
                new_word += letter
            else:
                new_word += letter
        print(new_word)

game_continue = True

while game_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    should_continue = input("Type yes if you want to continue or type no to stop the program.\n").lower()
    ceaser(direction=direction, text=text, shift=shift)
    if should_continue == "no":
        game_continue = False