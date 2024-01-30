import random

con_input = input("Enter consonant values separated by a space character >> ")
vow_input = input("Enter vowel values separated by a space character >> ")
pattern = input("Specify the pattern (either C or V) with no spaces, e.g. 'CVC' ")
num_words = input("Enter the number of words to generate")

con_list = con_input.split()
vow_list = vow_input.split()

def generate_word(syllable) :
    arr = []
    for x in syllable :
        if x == 'C':
            arr.append(random.choice(con_list))
        elif x == 'V':
            arr.append(random.choice(vow_list))
        else:
            print("Pattern elements must either be 'C' or 'V'. This element has defaulted to 'V'")
            arr.append(random.choice(vow_list))
    word = ''.join(arr)
    print(word)
    return word

for x in range(int(num_words)) :
    generate_word(pattern)