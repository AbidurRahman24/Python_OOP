def all_sum(num1, num2, *numbers):
    sum = 0 + num1 + num2
    for num in numbers:
        sum = sum + num
    return sum

total = all_sum(20,30,10,40)
print(total)

def famous_name(first, last, **addition):
    name = f' {first} {last}'
    # print(addition['title'])
    for key, value in addition.items():
        print(key, value)
    return name

name = famous_name(first='Taher', last='Ali', title="Hujur", title2="Shayokh", last2='taheri')
print(name)
