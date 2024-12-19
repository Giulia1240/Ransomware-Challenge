import os
import pyaes

# Abrir arquivo criptografado
file_name = 'teste.txt.ransomwaretroll'
file_open = open(file_name, 'rb')
file_data = file_open.read()
file_open.close()

# Definir a chave de descriptografia
key = b'testeransomwares'
aes = pyaes.AESModeOfOperationCTR(key)

# Descriptografar o arquivo
decrypt_data = aes.decrypt(file_data)

# Descarte do arquivo criptografado
os.remove(file_name)

# Criar arquivo descriptografado
new_file_name = "teste.txt"
with open(new_file_name, "wb") as new_file:  
    new_file.write(decrypt_data)
