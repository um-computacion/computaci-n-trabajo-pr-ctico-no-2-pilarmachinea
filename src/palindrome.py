import re

def is_palindrome_basic(text: str) -> bool:
    return text == text[::-1]

def clean_text(text: str) -> str:
    text = text.lower().strip()
    # Eliminar caracteres no alfanuméricos
    return re.sub(r'[^a-z0-9]', '', text)

def is_palindrome(text: str) -> bool:
    cleaned = clean_text(text)
    return is_palindrome_basic(cleaned)

if __name__ == '__main__':
    frase = input("Ingrese una palabra o frase: ")
    if is_palindrome(frase):
        print(f'"{frase}" es un palíndromo')
    else:
        print(f'"{frase}" no es un palíndromo')
