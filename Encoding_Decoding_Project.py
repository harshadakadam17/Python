alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction=input("Please enter 'encode' to encrpt and 'decode' to decrypt :\n ").lower()
text=input("Please enter your message:\n").lower()
shift=int(input("Pleases enter shift number :\n "))

def encrpt(original_text,shift_text):
    for letters in original_text:
        shifted_position=alphabet.index(letters)+shift_ammount
        alphabet[shifted_position]
    