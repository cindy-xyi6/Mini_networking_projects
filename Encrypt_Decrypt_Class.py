import string

class Encrypt_Decrypt:
    
    def __init__(self, encrypt_increment):
        # only create a [ self.x ] if you want to share the information among the functions.
        self.encrypt_increment = encrypt_increment

    def Encrypt(self, message):
        # Turns text into a list
        info = list(message)

        # Converting char into ascii char values
        ascii_values = []
        index = 0 
        for index in range(len(info)):
            info_letter = info[index]
            # ord converts letters into ascii char values / (unicode).
            ascii_char = ord(info_letter)
            ascii_values.append(ascii_char)
            index += 1

        """
        1. Get the index of each char in the ascii_values list.
        2. Add the number [encrypt_increment] to the chars ascii value.
        3. Change char values into letters.
        """

        # Tokenizing
        index = 0
        encrypted_ascii_char_value = []
        for index in range(len(message)):
            ascii_char_value = ascii_values[index]
            if (ascii_char_value == 10):
                # Leaves the eol(end of line) ascii char value alone.
                encrypted_ascii_char_value.append(10)
            else:
                new_letter_num = (ascii_char_value + self.encrypt_increment)
                # Using ascii value range 127(the last character value of a ascii table).
                if (new_letter_num > 127):
                    # -97 so value does not go below 32(space), so other commands arent included.
                    equ = (new_letter_num - 97)
                    # Add the encrypted character value to the list.
                    encrypted_ascii_char_value.append(equ)
                else:
                    encrypted_ascii_char_value.append(new_letter_num)
                    
            index +=1

        # Changing ascii char value into the ascii char. 
        encrypted = ""
        index2 = 0
        for index2 in (encrypted_ascii_char_value):
            #The chr() function returns the corresponding character or string.
            encrypted = encrypted + chr(index2)
            index2 += 1

        return (str(encrypted))


    def Decrypt(self, message):
        decrypt_increment = self.encrypt_increment
        encrypted_characters = list(message) 

        #Converting characters into ascii values
        decrypt_values = []
        index = 0 
        for index in range(len(message)):
            ascii_char = encrypted_characters[index]
            ascii_char_values = ord(ascii_char)
            # ascii values to be decrypted are stored in the decrypt_values list.
            decrypt_values.append(ascii_char_values)

            index += 1

        index = 0
        # values that are decrypted are stored in the list decrypted_values.
        decrypted_values= []
        for index in range(len(message)):
            # The individual characters to be decrypted are known as the ascii_char.
            ascii_char = decrypt_values[index]
            if (ascii_char == 10):
                # Leaves eol value alone.
                decrypted_values.append(10)
            else:
                # The individual ascii character that has been decrypted is known as decrypted_char.
                decrypted_char = (ascii_char - decrypt_increment)

                if (decrypted_char < 32):
                    equ = (decrypted_char + 97)
                    decrypted_values.append(equ)
                else: 
                    decrypted_values.append(decrypted_char)
            index +=1

        #changing ascii into letter 
        decrypted = ""
        index2 = 0
        for number in decrypted_values:
            decrypted = decrypted + chr(number)
            index2 +=1

        return (str(decrypted))

