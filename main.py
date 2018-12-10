import decimal

new_list = []
x = 2
while x <= 5.5:
    y = str(x)
    new_list.append(decimal.Decimal(y))
    x += 0.5

print(new_list)
print(type(new_list[0]))