# LIST is a collection which is ordered and changeable. Allows duplicate members.
import this


numbers = [1, 3, 5, 7, 9]
names = ["Tomek", "Kasia", "Basia", "Bartek", 'Jan']
print("Numbers", numbers) 
print("Names", names)

numbers.append(2)
numbers.append(7)

names.append("Adam")
names.append("Agata")

numbers.sort()
numbers.reverse()
names.pop(1)
names.remove("Jan")

print("Numbers", numbers) 
print("Names", names)

# TUPLE is a collection which is ordered and unchangeable. Allows duplicate members.
tuple_list_cities = ("Paris", "Porto", "Wroclaw")
tuple_list_different_types = ("Jan", 34, True)
print(type(tuple_list_cities))
print(type(tuple_list_different_types))

# SET is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
myset = {"banan", "cytryna", "kiwi", "kiwi"}
thisset = (("banan", "cytryna", "kiwi", "kiwi"))
print(type(myset))
print(type(this))

# SET - Union
first_set = {"A", "B", "C" , "D"}
second_set = {"B", "E", "F"}
union = first_set | second_set
print(f"union = {union}")

# SET - Intersection
intersection = first_set & second_set
print(f"intersection = {intersection}")

# SET - Difference
difference_A = {"a", "b", "c"}
difference_B = {"c", "d", "e"}
difference_result_A = difference_A - difference_B
difference_result_B = difference_B - difference_A
print(f"difference_result_A = {difference_result_A}")
print(f"difference_result_B = {difference_result_B}")

# DICTIONARY is a collection which is ordered** and changeable. No duplicate members. Key and value.
mydict = {
    "Polska" : " Poznan",
    "Hiszpania" : "Barcelona",
    "Norwegia" : "Oslo"
}
print(type(mydict))