from sympy import mod_inverse
from django import forms


def decrypt(encrypt_text, k0, k1):
    print(encrypt_text)
    text = list(encrypt_text.upper().replace(" ", ""))
    result = ""
    for i in range(len(text)):
        text[i] = chr(((k1 * (ord(text[i]) - ord("A")) + k0) % 26) + ord("A"))
        result = result + text[i]
    return result


def encrypt(plain_text, k0, k1):
    print(plain_text)
    text = list(plain_text.upper().replace(" ", ""))
    print(len(text))
    result = ""
    modinv = mod_inverse(k1, 26)
    for i in range(len(text)):
        text[i] = chr((modinv * ((ord(text[i]) - ord("A")) - k0)) % 26 + ord("A"))
        result = result + text[i]
    return result


class affineForm(forms.Form):
    text = forms.CharField()
    k0 = forms.CharField()
    k1 = forms.CharField()


# def main():
#     your_text = "AFFINEcipher"
#     k0 = 10  # int number
#     k1 = 3  # select from >>> 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25
#     print(
#         "ENCRYPTED : "
#         + encrypt(your_text, k0, k1)
#         + "\nPLAIN_TEXT : "
#         + decrypt(encrypt(your_text, k0, k1), k0, k1)
#     )


# if __name__ == "__main__":
#     main()