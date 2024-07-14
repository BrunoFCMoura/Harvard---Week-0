def convert(space):
    return space.replace(" ", "...")

def main():
    user_input = input(" ")
    print(convert(user_input))

if __name__ == "__main__":
    main()
