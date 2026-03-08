stack = []

while True:
    number = input("Put the number to store and will break if entered character : ")
    try:
        number = int(number)
        stack.append(number)
    except:
        break

smallest_num = min(stack)
print(smallest_num)