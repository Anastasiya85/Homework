# наименьшее число
a = int (input (5))
b = int (input (8))
c = int (input (15))
m = c
if m < b:
    m = b
    if m < a:
        m = a
        print (m)

# наибольшее число
a = int (input (5))
b = int (input (8))
c = int (input (15))
k = a
if k > b:
    k = b
    if k > c:
        k = c
        print (k)
