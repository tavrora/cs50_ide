from cs50 import get_int

# request and input validation
while True:
    h = get_int("Height: ")
    if h > 0 and h < 9:
        break

# drawing a pyramid
for i in range(1, h + 1):
    print(" " * (h - i), end="")
    print("#" * i, end="")
    print("  ", end="")
    print("#" * i)