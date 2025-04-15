def is_palindrome(text: str) -> bool:
    return text == text[::-1]

if __name__ == '__main__':
    frase = input("Ingrese una palabra o frase: ")
    if is_palindrome(frase):
        print(f'"{frase}" es un palíndromo')
    else:
        print(f'"{frase}" no es un palíndromo')
