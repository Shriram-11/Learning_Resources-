import hashlib
string = "hello world"
encoded = string.encode()
result = hashlib.sha256(encoded)
print("String : ", end="")
print(string)
print("Hash Value : ", end="")
print(result)


# b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9
