main_list = [12, 3, 45, 8, 19, 22, 5, 30, 17, 2, 
             "яблуко", "груша", "апельсин", "вишня", "банан", 
             "ківі", "персик", "лимон", "малина", "диня"]
a = []
b = []
two = []
upp = []

for i in main_list:
    if type(i) == int:
        a.append(i)
    elif type(i) == str:
        b.append(i)

sort_list = sorted(a) + sorted(b)

for i in sort_list:
    if type(i) == str:
        continue
    elif i % 2 == 0:
        two.append(i)

for i in sorted(b):
    upp.append(i.upper())

print("main_list (початковий список):", main_list)
print("sort_list (відсортовані числа та слова):", sort_list)
print("two (парні числа зі списку):", two)
print("upp (слова у верхньому регістрі):", upp)