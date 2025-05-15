def count_words(data):
    words = data.split()
    return len(words)


def count_characters(data):
    count_dict = {}
    for character in data:
        if character.lower() not in count_dict.keys():
            count_dict[character.lower()] = 1
        else:
            count_dict[character.lower()] += 1
    count_list = []
    for pair in count_dict.items():
        if pair[0].isalpha():
            count_list.append({"char": pair[0], "num": pair[1]})
    return count_list


def sort_on(dict):
    return dict["num"]