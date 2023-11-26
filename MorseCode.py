# Morse Code Encoder/Decoder

# morse table for encoding
morse_table = {
  'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
  'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
  'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
  'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
  'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
  '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
  '6': '-....', '7': '--...', '8': '---..', '9': '----.',
  '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
  ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
  '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
}
# inverted version of the morse table for decoding
inv_mt = dict(zip(morse_table.values(), morse_table.keys()))

def decode_morse(msg):
    # split words/chars from input
    pword = msg.split("   ")
    pchar = []
    for word in pword:
        pchar.append(word.split(" "))
    
    # check valid inputs 

    # decode
    decoded_msg = []
    for word in pchar:
        for char in word:
            if char in inv_mt.keys():      # discard non recognised sequences
                decoded_msg.append(inv_mt.get(char))
        decoded_msg.append(" ")
    output = "".join(decoded_msg)
    return output

def encode_morse(msg):
    encoded_msg = []
    for char in msg:
        if char in morse_table.keys():      # discard any non supported characters/symbols
            encoded_msg.append(morse_table.get(char))
    output = " ".join(encoded_msg)
    return output

# user interface
command = ""
while command != "exit":
    command = str(input("""
-------------------------
    Select Operation: 
-------------------------
                        
encode      (Encode Morse)
decode      (Decode Morse)               
exit        (Exit Program)
                        
> """))
    #exit
    if command == "exit":
        break

    #encode
    elif command == "encode":
        e_msg = str(input("\nEnter text to be encoded:\n\n> "))
        print(f"""
-------------------------
     Encoded Message:
------------------------- 
                           
{encode_morse(e_msg.upper())}""")

    #decode
    elif command == "decode":
        d_msg = str(input("\nEnter Morse message to be decoded\nCharacters should be seperated by one space, Words seperated by three spaces\nExample: -.-- --- ..-   .- .-. .   ... --- ..- .-..\n\n> "))
        print(f"""
-------------------------
     Decoded Message:
------------------------- 
                           
{decode_morse(d_msg.upper())}""")

    #invalid input
    else:
        print("ERROR: INVALID INPUT")
