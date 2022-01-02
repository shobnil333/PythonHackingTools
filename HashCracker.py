import hashlib, termcolor


type_of_hash = str(input('Enter salt/type of hash: '))
input_file = str(input('Enter Password file: '))
hash_to_decrypt = str(input('Enter hash to decrypt: '))

with open(input_file, 'r') as file:
    for line in file.readlines():
        valid_pass = line.strip()
        if type_of_hash == 'md5':
            hash_object = hashlib.md5(valid_pass.encode())
            hashed_word = hash_object.hexdigest()
            if hashed_word == hash_to_decrypt:
                print('[+] Valid Password Found', termcolor.colored(valid_pass, 'green'))
                exit(0)
        elif type_of_hash == 'sha256':
            hash_object = hashlib.sha256(valid_pass.encode())
            hashed_word = hash_object.hexdigest()
            if hashed_word == hash_to_decrypt:
                print('[+] Valid Password Found', termcolor.colored(valid_pass, 'green'))
                exit(0)
