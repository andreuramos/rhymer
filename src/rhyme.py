import sys

from Application.RhymeUseCase import RhymeUseCase
from Application.RhymeRequest import RhymeRequest


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python app.py <word>")
        sys.exit(1)

    word = sys.argv[1]
    request = RhymeRequest(word=word)
    result = RhymeUseCase().execute(request=request)

    if len(result.words):
        print(f"Word {word} is in the dictionary")
    else:
        print(f"Word {word} is NOT in the dictionary")
