def spin_words(sentence):
    tokens = sentence.split(' ')
    new_sentence = []
    for token in tokens:
            if len(token) > 4:
                new_token = []
                for letter in token[::-1]:
                    new_token.append(letter)
                new_token = "".join(new_token)
                print(new_token)
                new_sentence.append(new_token)
            else:
                new_sentence.append(token)

    #print(new_sentence)
    new_sentence = " ".join(new_sentence)
    return new_sentence