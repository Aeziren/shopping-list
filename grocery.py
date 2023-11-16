items = {}
while True:
    try:
        item = input().strip().lower()
    except EOFError:

        for item in sorted(items):
            print(f"{items[item]} {item.upper()}")

        break
    else:
        if item not in items:
            items[item] = 1
        else:
            items[item] += 1


