import sys
from string import ascii_lowercase as lc

file = open(sys.argv[1], 'r').read().lower()
key = sys.argv[2].lower()
mode = sys.argv[3]


def help():
    print(' Modo de uso: \n'
          'CIFRAR: python vigenere.py {caminho/arquivo com o conteúdo de texto} {chave para encriptar} {modo de uso: enc} \n'
          'DECIFRAR: python vigenere.py {caminho/arquivo com o conteúdo de texto} {chave para decifrar} {modo de uso: dec} \n'
          'Exemplo para encriptar --> python vigenere.py texto.txt senha enc \n'
          'Exemplo para decifrar --> python vigenere.py texto.txt senha dec ')


def vigenere_encrypt(file, key):
    resultado = ''
    keyidx = 0
    for letra in file:
        if letra in lc:
            index = lc.find(letra)
            index += lc.find(key[keyidx % len(key)])  # SOMA A POSIÇÃO DA LETRA DO TEXTO COM A POSIÇÃO DA LETRA DA CHAVE DE ENCRIPTAÇÃO
            resultado += lc[index % 26]
            keyidx += 1
        else:
            resultado += letra
    print(resultado)
    file2 = open('ciphertext.txt', 'a+')
    file2.write(resultado)
    file2.close()


def vigenere_decrypt(file, key):
    resultado = ''
    keyidx = 0
    for letra in file:
        if letra in lc:
            index = lc.find(letra)
            index -= lc.find(key[keyidx % len(key)])
            resultado += lc[index % 26]
            keyidx += 1
        else:
            resultado += letra
    print(resultado)
    file2 = open('plaintext.txt', 'a+')
    file2.write(resultado)
    file2.close()


if mode == 'enc':
    vigenere_encrypt(file, key)
elif mode == 'dec':
    vigenere_decrypt(file, key)
else:
    help()

