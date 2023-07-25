# python Anatomy Of Email
email = "lyb900702@gmail.com"
index = email.index('@')
print(index)
print(f'username : {email[:index]}')
print(f"domain : {email[index+1:]}")
