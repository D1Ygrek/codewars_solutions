class VigenereCipher(object):
    __key: None
    __alphabet: None

    def __init__(self, key, alphabet):
        self.__key = key
        self.__alphabet = alphabet
    
    def encode(self, text):
        need_key_len = len(text)
        return_text = ""
        for i in range(need_key_len):
            key_simbol = self.__key[i % len(self.__key)]
            symbol_number = self.__alphabet.find(text[i])
            if symbol_number!=-1:
                key_simbol_number = self.__alphabet.find(key_simbol)
                return_text+=self.__alphabet[(symbol_number+key_simbol_number)%len(self.__alphabet)]
            else:
                return_text+=text[i]
        return return_text
    def decode(self, text):
        need_key_len = len(text)
        return_text = ""
        for i in range(need_key_len):
            key_simbol = self.__key[i % len(self.__key)]
            symbol_number = self.__alphabet.find(text[i])
            if symbol_number!=-1:
                key_simbol_number = self.__alphabet.find(key_simbol)
                return_text+=self.__alphabet[(symbol_number-key_simbol_number)%len(self.__alphabet)]
            else:
                return_text+=text[i]
        return return_text

abc = "abcdefghijklmnopqrstuvwxyz"
key = "password"
c = VigenereCipher(key, abc)

print(c.encode('codewars'))
print(c.decode('rovwsoiv'))

print(c.encode('waffles'))
print(c.decode('laxxhsj'))

print(c.encode('CODEWARS'))
print(c.decode('CODEWARS'))