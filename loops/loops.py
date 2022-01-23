# For loop
numbers = [1, 3, 5, 6, 7, 9]
sum = 0

for item in numbers:
    sum += item

print(f"Sum = {sum}")

my_list = {
    1 : "one", 
    2 : "two",
    3 : "three"    
}

for key, value in my_list.items():
    print(f"Key = {key} : Value = {value}")

# While loop
names = ["Kasia", "Agata", "Tomek", "Bartek", "Adam"]
item = 0

while item < len(names):
    print(names[item])
    item +=1

# Break
item = 0
for item in range(6):
    if item == 4:
        break
    print(f"item = {item}")

# Continue
item = 0
while item < 10:
    item += 1
    if item == 5:
        continue
    print(f"item = {item}")