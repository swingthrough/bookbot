def get_num_of_words(text):
    words = text.split()
    return len(words)

def get_char_counts_dict(text):
    char_counts = {}

    for char in text:
        lowercase_char = char.lower()
        if lowercase_char not in char_counts:
            char_counts[lowercase_char] = 1
        else:
            char_counts[lowercase_char] += 1

    return char_counts



def char_counts_dict_to_sorted_list(char_counts):
    def sort_on(dict):
        return dict["count"]
    
    list_of_dicts = []

    for char in char_counts:
        list_of_dicts.append({
            "char": char,
            "count": char_counts[char]
        })

    list_of_dicts.sort(key=sort_on, reverse=True)
    
    return list_of_dicts