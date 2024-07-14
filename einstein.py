#E=m.c²
def main():
    m = int(input("m:"))
    E = (m * square(300000000))
    print("E: "f"{E:,}")

def square(n):
    return n * n

main()
