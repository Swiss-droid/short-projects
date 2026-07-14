name = input("Enter your name: ")
last_name = input("Enter your surname: ")
bio = input("Enter your bio: ")
new_bio = bio.replace("I am", "I'm") # replaces the I am with I'm in the bio
username = f"{name[0]} {last_name}"
full_name = f"{name} {last_name}"

print(name)
print(last_name)
print(bio)
print(len(bio)) # length of the bio
print(new_bio)
print(username)
print(full_name.title())