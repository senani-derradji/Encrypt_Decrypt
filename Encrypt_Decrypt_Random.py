import random, string, datetime
current_datetime = datetime.datetime.now()
hour, minute, second = current_datetime.hour, current_datetime.minute, current_datetime.second
time = f"{hour}/{minute}/{second}"
print(time)
def generate_random_value(k):
    return ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=k))
def generate_random_dictionary(k_const):
    random_dict = {}
    keys = string.ascii_lowercase + string.digits + string.punctuation
    for key in keys:
        random_dict[key] = generate_random_value(k_const)
    return random_dict
k_const = int(input("K = "))
text = str(input("Text = "))
random_dict = generate_random_dictionary(k_const)
inverse_dict = {value: key for key, value in random_dict.items()}
with open(f"{time}.txt", "w") as file:
    file.write("----------------------Key Encrypt------------------\n")
    file.write(f"{random_dict}")
    file.write("\n\n")
    file.write("------------------Key Decrypt------------\n")
    file.write(f"{inverse_dict}")
encrypted_text = "".join(random_dict[char] for char in text if char in random_dict)
def decrypt(text):
    if len(text)%k_const == 0:
        chunks = [text[i:i+k_const] for i in range(0, len(text), k_const)]
        replaced_text = [inverse_dict[item] for item in chunks]
    else:
        chunks = ""
        replaced_text = ""
    return ''.join(replaced_text)
print(text)
print(random_dict)
print(encrypted_text)
print(decrypt(encrypted_text))
