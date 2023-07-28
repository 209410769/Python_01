# def hello(greeting,title,first_name,last_name):
#     print(f"{greeting},{title},{first_name},{last_name}")

# hello("Hello","Mr","Jimmy","Lin")
# hello(greeting="Hello!",title="Mr",first_name="Jimmy",last_name="Lin")

def get_phone(country_code,area_code,first,last):
    return f"{country_code}-{area_code}-{first}-{last}"
str = get_phone(country_code="886",area_code="02",first="2723",last="9999")

print(str)