def get_word_count(file_path):

    with open(file_path) as f:
        contents = f.read()

    num_of_words = len(contents.split())

    print(f"Found {num_of_words} total words")

def get_char_count(file_path):

    with open (file_path) as f:
        contents = f.read()
    
    char_dict = {}

    for char in contents:
        lower_char = char.lower()
        if lower_char not in char_dict:
            char_dict[lower_char] = 1
        else:
            char_dict[lower_char] += 1

    return char_dict

def sort_on(dict):
    return dict["num"]

def sorted_list(dict):
    listed_dicts = []

    for i in dict:
        if i.isalpha() == False:
            continue
        temp_dict = {}
        temp_dict["char"] = i
        temp_dict["num"] = dict[i]
        listed_dicts.append(temp_dict)

    listed_dicts.sort(reverse=True, key=sort_on)
    
    for dict in listed_dicts:
        print(f"{dict["char"]}: {dict["num"]}")
