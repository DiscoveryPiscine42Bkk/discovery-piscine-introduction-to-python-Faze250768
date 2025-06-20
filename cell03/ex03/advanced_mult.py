import sys

def print_table(n):
    print(f"Table de {n}:", end=" ")
    for i in range(11):
        print(n * i, end=" ")
    print()

if len(sys.argv) == 1:
    for i in range(11):
        print_table(i)
else:
    try:
        n = int(sys.argv[1])
        print_table(n)
    except:
        print("none", end="")
