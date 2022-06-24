words = ['dog', 'cat', 'horse', 'goat', 'cat', 'horse', 'fish', 'dog', 'dog', 'fish']


def find():
    freq = []
    uwrd = []
    i = 0
    count = 0
    if len(words) == 0:
        print('Please enter some words!')
        return -1
    for wrd in words:
        is_uniq = True
        for un_word in uwrd:
            if wrd == un_word:
                is_uniq = False
        if is_uniq:
            uwrd.append(wrd)

    for un_word in uwrd:
        for wrd in words:
            if un_word == wrd:
                count = count + 1
        freq.append(count)
        count = 0

    for un_word in uwrd:
        print(un_word + ' ' + str(freq[i]))
        i = i + 1


if __name__ == '__main__':
    find()
