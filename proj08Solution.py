
import itertools
from operator import itemgetter

SCORE_DICT = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, \
              'i': 1, 'j': 8, 'k': 8, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, \
              'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, \
              'y': 4, 'z': 10}

def open_file():
        
    while True:
        try:
            filename = input('Input word file: ')
            fp = open(filename, 'r')
            return fp
        except FileNotFoundError:
            print("File not found. Try again.")
            

def read_file(fp):
    D = {}
    for line in fp:
        phrase = line.strip().lower()
        if len(phrase) >= 3 and '-' not in phrase and "'" not in phrase:
            D[phrase] = 1
            
    return D

        
def calculate_score(rack,word):
    score = 0
    count = 0
    N = len(rack)
    for ch in word:
        score += SCORE_DICT[ch]
        if ch in rack:
            rack = rack.replace(ch,'',1)
            count += 1

    if len(rack) == 0 and N == 7:
        score += 50
    return score
    


def generate_combinations(rack,placed_tile):
    combinations = set()
    new = rack + placed_tile
    for i in range(3,len(new)+1):
        for x in itertools.combinations(new, i):
            if placed_tile in x or placed_tile == '':
                combinations.add(x)
    return combinations
        

        

def generate_words(combo,scrabble_words_dict):    
    """
    Insert function header
    """
    words =set()
    for word in itertools.permutations(combo):
        word = ''.join(word)
        if word in scrabble_words_dict:
            words.add(word)
            
    return words


def generate_words_with_scores(rack,placed_tile,scrabble_words_dict):
    """
    Insert function header
    """
    D ={}
    combinations = generate_combinations(rack,placed_tile)
    for combo in combinations:
        words = generate_words(combo,scrabble_words_dict)
        for word in words:
            D[word] = calculate_score(rack,word)
    return D
    
    

def sort_words(word_dic):
    """
    Insert function header
    """
    word_lst=[]
    for word,score in word_dic.items():
        word_lst.append((word,score,len(word)))
    word_lst = sorted(word_lst,key=itemgetter(0))  
    score_sort = sorted(word_lst,key=itemgetter(1,2),reverse=True)
    length_sort = sorted(word_lst,key=itemgetter(2,1),reverse=True)
    
    return score_sort,length_sort
    

def display_words(word_list,specifier):
    """
    Insert function header
    """
    if specifier == 'score':
        sort_index = 1
    else:
        sort_index = 2
    
    print("{:>6s}  -  {:s}".format(specifier.title(),'Word'))
    for tup in word_list[:5]:
        print("{:>6d}  -  {:s}".format(tup[sort_index],tup[0]))

    

def main():
    print("Scrabble Tool")
    
    choice = input("Would you like to enter an example (y/n): ")
    while choice == 'y':
        fp = open_file()
        scrabble_words_dict = read_file(fp)
        rack = input("Input the rack (2-7chars): ")
        while not (rack.isalpha() and 2<=len(rack)<=7):
            print("Error: only characters and 2-7 of them. Try again.")
            rack = input("Input the rack (2-7chars): ")
        
        placed_tiles = input("Input tiles on board (enter for none): ")
        while not (placed_tiles.isalpha() or  placed_tiles == ''):
            print("Error: tiles must be characters or empty")
            placed_tiles = input("Input tiles on board (enter for none): ")
        word_dic = {}
        if placed_tiles == '':
            word_dic.update(generate_words_with_scores(rack,placed_tiles,scrabble_words_dict))
        else:
            for placed_tile in placed_tiles:
                word_dic.update(generate_words_with_scores(rack,placed_tile,scrabble_words_dict))
        
        score_sort,length_sort = sort_words(word_dic)
        
        print('Word choices sorted by Score')
        display_words(score_sort,'score')
        
        print('\nWord choices sorted by Length')
        display_words(length_sort,'length')

        choice = input("Do you want to enter another example (y/n): ")
    else:
        print("Thank you for playing the game")
    
 
if __name__ == "__main__":
     main()
