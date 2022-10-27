import math


def compute_entropy(file_name):
    # Read text file as bit string
    with open(file_name, "rb") as f:
        data = f.read()

    # Compute probability distribution of characters in text
    count = [0 for i in range(256)]
    for i in data:
        count[i] += 1
    n = len(data)
    p = [i / n for i in count]

    # Compute entropy by using probability distribution
    entropy = 0
    for i in p:
        if i != 0:
            entropy -= i * math.log2(i)
    print(f'The entropy of "{file_name}" is {entropy:.2f}.')
    return entropy


if __name__ == '__main__':
    en = compute_entropy("Clinton's speech.txt")
