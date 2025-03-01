def count_words(content):
    words_list = content.split()
    return len(words_list)

def character_count(content):
    char_dict = {}
    for char in content:
        lower_char = char.lower()
        if lower_char not in char_dict:
            char_dict[lower_char] = 1
        else:
            char_dict[lower_char] += 1
    return char_dict

def sort_key(d):
    return d["count"]

def char_dict_to_sorted_list(char_dict):
    sorted_list = []
    for char in char_dict:
        sorted_list.append({"char": char, "count": char_dict[char]})
    sorted_list.sort(reverse=True, key=sort_key)
    return sorted_list