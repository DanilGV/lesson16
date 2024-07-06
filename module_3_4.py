def single_root_words(root_word, *other_words):
    same_words = []

    root_word_upp = root_word.upper()

    for word in other_words:
        word_upp = word.upper()
        if word_upp in root_word_upp or root_word_upp in word_upp:
            same_words.append(word)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
