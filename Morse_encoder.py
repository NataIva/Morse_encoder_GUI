from tkinter import *
# ---------------------------- Morse code dict------------------------------- #
morse_code_dict_en = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
                 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
                 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
                 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
                 '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
                 '.': '.−.−.−', ',': '−−..−−', '!': '−.−.−−', '?': '..−−..', '"': '.−..−.', ';': '−.−.−.',
                 ':': '−−−...', '-': '−....−', '+': '.−.−.',  '=': '−...−', '_': '..−−.−', '/': '−..−.', '(': '−.−−.',
                 ')': '−.−−.−', '&': '.−...', '@': '.−−.−.', '$': '.−...', ' ': ' ', '\n': ''}

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Morse encoder by Glass cat")
window.config(padx=20, pady=20, bg="#9bdeac")
# lock size window
window.resizable(False, False)
frame = Canvas(width=390, height=300, bg="#9bdeac")
frame.grid(column=0, row=0, columnspan=2, rowspan=7)

# ----------------------Labels
label_type_message = Label(text="Type your message, my friend:", font="16", bg="#9bdeac")
label_type_message.grid(column=0, row=0, columnspan=2)
#
label_encoded_txt_place = Label(text=f'Encrypted message:', font="16", bg="#9bdeac")
label_encoded_txt_place.grid(column=0, row=3, columnspan=2)

# ----------------------Message and encrypted text
typed_message_field = Text(width=45, height=4, bg="white", wrap=WORD)
typed_message_field.grid(column=0, row=1, columnspan=2)
#
encrypted_text_field = Text(width=45, height=4, bg="white", wrap=WORD)
encrypted_text_field.grid(column=0, row=4, columnspan=2)

# ----------------------Button encrypt
def encrypt():
    # clear encrypted field
    encrypted_text_field.delete(1.0, END)
    text_message = typed_message_field.get(1.0, END)
    text_message_split = []
    for letter in text_message:
        text_message_split.append(letter.capitalize())
    encode_in_morse = []
    symbol_not_in_dict = []
    for letter in text_message_split:
        if letter in morse_code_dict_en:
            encode_in_morse.append(morse_code_dict_en[letter])
        else:
            symbol_not_in_dict.append(letter)
    if len(symbol_not_in_dict) > 0:
        alert_sms ='You can use only letters of the English alphabet, numbers and \nthe following characters: ' \
                   '. , ! ? / - + = @ $ & () _ : ; "'
        encrypted_text_field.insert(1.0, alert_sms)
    else:
        text_for_label = ''.join(encode_in_morse)
        encrypted_text_field.insert(1.0, text_for_label)

encrypt_button = Button(height=1, width=8, text="Encrypt", font="16",  bg="lightgrey",
                        command=encrypt, activebackground='white')
encrypt_button.grid(column=0, row=2)

# ----------------------Button clear
def clear_field():
    # clear both fields
    typed_message_field.delete(1.0, END)
    encrypted_text_field.delete(1.0, END)

clear_button = Button(height=1, width=8, text="Clear", font="16", bg="lightgrey", activebackground='white', command=clear_field)
clear_button.grid(column=1, row=2)

# ----------------------Button copy
def return_button_copy():
    copy_button.config(text='Copy')

def copy_func():
    copy_text = encrypted_text_field.get(1.0, END)
    # clear buffer (clipboard)
    encrypted_text_field.clipboard_clear()
    # insert text to buffer (clipboard)
    encrypted_text_field.clipboard_append(copy_text)
    copy_button.config(text="Copied")
    window.after(700, return_button_copy)

copy_button = Button(height=1, width=8, text="Copy", font="16", activebackground='white',
                     command=copy_func, bg="lightgrey")
copy_button.grid(column=0, row=5, columnspan=2)


window.mainloop()
