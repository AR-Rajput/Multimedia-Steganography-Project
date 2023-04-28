hidden_message = input("Enter the hidden message: ")

hm_binary = "".join(format(ord(i), "08b") for i in str(hidden_message))

print(hm_binary)