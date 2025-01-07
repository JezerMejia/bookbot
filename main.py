def count_repeated(text: str) -> dict[str, int]:
    repeated = {}
    for char in text:
        lower = char.lower()
        if lower not in repeated:
            repeated[lower] = 1
        else:
            repeated[lower] += 1

    return repeated

def sort_on(dict):
    return dict[1]

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

        repeated = count_repeated(file_contents)
        repeated = list(repeated.items())
        repeated.sort(reverse=True,key=sort_on)
        words = file_contents.split()

        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{len(words)} words found in the document\n")

        for (char, value) in repeated:
            if char.isalpha():
                print(f"The '{char}' character was found {value} times")

        print("--- End report ---")

main()
