import sys

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python app.py <word>")
        sys.exit(1)

    word = sys.argv[1]
    print(f"Word is {word}")
