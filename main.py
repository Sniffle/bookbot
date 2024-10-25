def main():
    path = "books/frankenstein.txt"
    with open(path) as f:
        file_contents = f.read()
        #print_all(file_contents) #works
        #count_words(file_contents) #works
        #letter_count = count_letters(file_contents) # works
        #print(letter_count)
        report(file_contents, path)

def print_all(text): #prints all contents of the file
    print(text)


def count_words(text):  #word count based on white space
    words = text.split() 
    return(len(words)) #return the word count to the calling function

def count_letters(text):
    lowered = text.lower()
    letters = {}

    for character in lowered:
        if character not in letters:
            letters[character] = 0
        letters[character] += 1
    return letters #print(letters) #pass letters to the function that calls it

def sort_on(dict):
    return dict["num"]

def sort_by_count(dict):
    ### list of dictionaries ###
    letters_list = []

    for keys in dict:
        letters_dict = {}
        letters_dict["name"] = keys
        letters_dict["num"] = dict[keys]
        letters_list.append(letters_dict)

    #print("letters_List: ",letters_list)

    ### /list of dictionaries ###

    ### sorting work ###
    letters_list.sort(reverse=True, key=sort_on)
    #print("sorted_list: ", letters_list) #working
    ### /sorting work ###
    return letters_list

def report(file: list, path: str):
    letters = count_letters(file)
    count = count_words(file)
    sorted_letters = sort_by_count(letters)
    print(f"--- Begin report of {path}")
    print(count,"words found in the document\n")
    for i in range(len(sorted_letters)):

        #print(sorted_letters[i]["name"])
        #print(sorted_letters[i]["num"])
        if sorted_letters[i]["name"].isalpha():
            print(f"The {sorted_letters[i]["name"]} was found {sorted_letters[i]["num"]} times")
    print("--- End report ---")



main()