# First, install the library in your terminal: pip install cryptography
from random import randint
from cryptography.fernet import Fernet
lazy import functions.Base.system as system
class generate_crypt():
    def generate_code(long:int):
        code=""
        for i in range(long):
            code+=str(randint(0,9))
        return code
    def generate_chaine(long:int):
        chaine=""
        min=randint(0,1)
        for i in range(long):
            if min==1:
                chaine+=chr(randint(ord('A'),ord('Z')))
            else:
                chaine+=chr(randint(ord('a'),ord('z')))
        return chaine
    def gen_better(long:int):
        a=""
        for i in range(long):
            c=randint(0,1)
            if c==0:
                a=a+generate_crypt.generate_code(1)
            elif c==1:
                a=a+generate_crypt.generate_chaine(1)
        return a
    def ecrypt(data:str):
        key = Fernet.generate_key()
        fernet = Fernet(key)
        encrypted_data = fernet.encrypt(data.encode()).decode()
        return encrypted_data, key.decode()
    def decrypt(encrypted_data: str, key: str):
        fernet = Fernet(key.encode())
        decrypted_data = fernet.decrypt(encrypted_data.encode()).decode()
        return decrypted_data
    def output(file:str,text:str):
        encrypted_text, secret_key = generate_crypt.ecrypt(text)
        print(f"Encrypted Text: {encrypted_text}")
        print(f"Key (Keep secret!): {secret_key}\n")
        system.creat_file("","Key")
        system.creat_file("",file)
        system.overwrite("Key",secret_key)
        system.overwrite(file,encrypted_text)
    def open(file:str,key:str,txt:str):
        original_text = generate_crypt.decrypt(txt, key)
        print(f"Decrypted Text: {original_text}")
        system.overwrite(file,original_text)
        system.delete_file("","Key")
    def run(file:str,cry:bool):
        if cry:
            text=system.read(file)
            generate_crypt.output(file,text)
        elif not(cry):
            text=system.read(file)
            key=system.read("Key")
            generate_crypt.open(file,key,text)