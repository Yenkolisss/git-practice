# Простая программа: перевод числа в разные системы счисления
def convert(n: int) -> dict:
    return {"bin": bin(n)[2:], "oct": oct(n)[2:], "hex": hex(n)[2:].upper()}

if __name__ == "__main__":
    for n in (10, 255, 4616):
        print(n, convert(n))
