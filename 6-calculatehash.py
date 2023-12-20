#Python script to calculate the hash (MD5 or SHA256) of a file.

import hashlib

def calculate_file_hash(file_path, algorithm="md5"):
    hash_object = hashlib.md5() if algorithm.lower() == "md5" else hashlib.sha256()
    with open(file_path, 'rb') as file:
        while chunk := file.read(8192):
            hash_object.update(chunk)
    return hash_object.hexdigest()

# Example usage:
file_to_hash = "example.txt"
hash_value = calculate_file_hash(file_to_hash, algorithm="sha256")
print(f"SHA256 Hash of {file_to_hash}: {hash_value}")
