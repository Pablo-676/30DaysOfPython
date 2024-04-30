from hashlib import sha256
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Util.Padding import pad, unpad
import string
import random as rd

class User:
    def __init__(self, nome, email, senha):
        # Inicializa o objeto usuário com o nome, email e senha fornecidos
        self.nome = nome
        self.email = email
        # Hash da senha fornecida usando SHA-256 e armazenamento
        self.senha = self.hash_password(senha)
        # Inicializa um dicionário vazio para armazenar as senhas salvas
        self.senhas_salvas = {}

        # Gera um vetor de inicialização aleatório (IV) para o ciframento AES
        iv = Random.new().read(AES.block_size)
        # Cria um objeto cifra com uma chave gerada aleatoriamente e o IV
        key = self.generate_random_sequence(16).encode()
        # Cria um novo objeto cifra com a mesma chave e IV para descriptografar a mensagem
        self.cipher = AES.new(key, AES.MODE_CBC, iv)
        self.cipher2 = AES.new(key, AES.MODE_CBC, iv)

    def generate_random_sequence(self, length):
        # Gera uma sequência aleatória de letras ASCII do comprimento especificado
        letters = string.ascii_letters
        result_str = ''.join(rd.choice(letters) for i in range(length))
        return result_str

    def hash_password(self, password):
        # Hash da senha fornecida usando SHA-256 e retorno do digesto hexadecimal
        if password is not None:
            hashed_password = sha256(password.encode()).hexdigest()
            return hashed_password
        return None

    def save_password(self, servico, password):
         # Salva uma senha para um serviço específico (por exemplo, Gmail, Facebook)
        if password is not None:
            # Adiciona preenchimento à senha para um múltiplo de 16 bytes usando o preenchimento PKCS#7
            padded_password = pad(password.encode(), AES.block_size)
            # Criptografa a senha preenchida usando o objeto cifra AES
            ciphertext = self.cipher.encrypt(padded_password)
            # Armazena a senha criptografada no dicionário com a chave do serviço
            self.senhas_salvas[servico] = ciphertext

    def display_infos_user(self):
        # Solicita a senha do usuário para exibir suas informações
        password = input('Digite a sua senha: ')
        # Verifica se a senha inserida corresponde ao hash armazenado
        if self.hash_password(password) == self.senha:
            # Exibe as informações do usuário se a senha estiver correta
            print(f"Infos do usuario {self.nome}")
            print(f"\nNome: {self.nome} \nEmail: {self.email} \nSenha: {self.senha}")
        else:
            print('Senha Incorreta')

    def display_saved_passwords(self):
        # Solicita a senha do usuário para exibir suas senhas salvas
        password = input('Digite a sua senha: ')
        # Verifica se a senha inserida corresponde ao hash armazenado
        if self.hash_password(password) == self.senha:
            # Exibe as senhas salvas se a senha estiver correta
            print(f"\nSenhas slavas pelo usuario {self.nome}")
            if self.senhas_salvas:
                # Itere sobre as senhas salvas e descriptografe-as
                for servico, ciphertext in self.senhas_salvas.items():
                    #Descriptografe o texto cifrado e remove o preenchimento PKCS#7
                    decrypted_data = self.cipher2.decrypt(ciphertext)
                    unpadded_data = unpad(decrypted_data, AES.block_size)
                    plaintext = unpadded_data.decode()
                    print("{}: {}".format(servico, plaintext))
            else:
                print('Nenhuma senha salva')
        else:
            print('Senha Incorreta')


# Cria um novo objeto de usuário com o nome, email e senha especificados
user = User('Pedro Pascal', 'Prderinho@example.com', 'senha123')

# Salva as senhas do Gmail and Facebook
user.save_password('gmail', 'pedrinho123')
user.save_password('facebook', 'pedroo_$')

# Exibe as informações do usuario
user.display_infos_user()

# Exibe as senhas salvas pelo usuario
user.display_saved_passwords()

# Print the saved passwords dictionary
print(user.senhas_salvas)
