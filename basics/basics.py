# Variables
first_name = "Jan"
last_name = "Kowalski"
age = 21
salary = 4500.00
phone_number = "509-098-983"
isMan = True
names = ["Adam, Tomasz, Jan, Kasia, Basia"]

# Or
name: str = "Tom"   # → String 
isMale: bool = True # → Boolean
number: int = 35    # → Integer
PI: float = 3.14    # → Float (final)

# Datatypes
print(type(first_name))   # → <class 'str'>
print(type(last_name))    # → <class 'str'>
print(type(age))          # → <class 'int'>
print(type(phone_number)) # → <class 'str'>
print(type(isMan))        # → <class 'bool'>
print(type(names))        # → <class 'list'>
###
print(type(name))   # → <class 'str'>
print(type(isMale)) # → <class 'bool'>
print(type(number)) # → <class 'int'>
print(type(PI))     # → <class 'float'>

# Concatenation
full_name: str = first_name + " " + last_name
print(type(full_name))

# Multiline and Formatting Strings
print("This is", first_name, last_name, "\nhe's", age, "\nhis phone number is", phone_number)
print(f"""
This is, {first_name} {last_name}
He is {age}
His phone number is {phone_number} 
""")

# Example Function
print(full_name.upper())
print(full_name.lower())
print(full_name.replace("Kowalski", "Nowak"))
print("Length", len(full_name))