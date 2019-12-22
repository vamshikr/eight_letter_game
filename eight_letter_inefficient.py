import sys


def create_dict(dict_file):
    word_dict = set()

    with open(dict_file) as fobj:

        for line in fobj:
            line = line.strip()
            word_dict.add(line)

    return word_dict


def swap(word, i, j):
    if i == j:
        return word
    else:
        return word[:i] + word[j] + word[i+1:j] + word[i] + word[j+1:]


def permutation(wdict, word, i):

    if (i == len(word) - 1) and word in wdict:
        yield word
    else:
        for j in range(i, len(word)):
            new_word = swap(word, i, j)
            yield from permutation(wdict, new_word, i+1)


def main(dict_file, words):
    word_dict = create_dict(dict_file)

    for word in words:
        print()
        for perm in set(permutation(word_dict, word.lower(), 0)):
            print(perm)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2:])
