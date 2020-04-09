import unittest
from proj08 import calculate_score, generate_combinations, generate_words, generate_words_with_scores, read_file, sort_words

class TestProject1(unittest.TestCase):

    def test_calculate_score(self):

        rack = 'tburett'
        word = 'butter'
        inst_score = 8
        stu_score = calculate_score(rack,word)
        print("rack,word:",rack,word)
        print("Instructor score:",inst_score)
        print("Student score   :",stu_score)
        assert inst_score == stu_score
        # test 7-char word with 7 tiles in rack
        rack = 'abteyrt'
        word = 'battery'
        inst_score = 62
        stu_score = calculate_score(rack,word)
        print("rack,word:",rack,word)
        print("Instructor score:",inst_score)
        print("Student score   :",stu_score)
        assert inst_score == stu_score
        # test 7-char word with less than 7 tiles in rack
        rack = 'abteyr'
        word = 'battery'
        inst_score = 12
        stu_score = calculate_score(rack,word)
        print("rack,word:",rack,word)
        print("Instructor score:",inst_score)
        print("Student score   :",stu_score)
        assert inst_score == stu_score


    def test_generate_combinations(self):
    
        rack = 'abc'
        placed_tile = 'x'
        inst_S = {('a', 'b', 'x'), ('a', 'b', 'c', 'x'), ('a', 'c', 'x'), ('b', 'c', 'x')}
        stu_S = generate_combinations(rack,placed_tile)
        print("rack, placed_tile:", rack, placed_tile)
        print("Instructor:",inst_S)
        print("Student   :",stu_S)
        assert inst_S == stu_S
        rack = 'abc'
        placed_tile = ''
        inst_S = {('a', 'b', 'c')}
        stu_S = generate_combinations(rack,placed_tile)
        print("rack, placed_tile:", rack, placed_tile)
        print("Instructor:",inst_S)
        print("Student   :",stu_S)
        assert inst_S == stu_S
        inst_S = {('t', 'r', 'e', 't', 'u'), ('t', 'b', 't', 'u'), ('y', 'r', 'e', 't', 't', 'u'), ('b', 'y', 'r', 'e', 'u'), ('t', 'b', 'e', 't', 't', 'u'), ('y', 'e', 't', 't', 'u'), ('t', 'b', 'r', 'e', 't', 'u'), ('t', 'b', 'u'), ('y', 'e', 'u'), ('b', 'y', 'e', 'u'), ('t', 'b', 'y', 't', 't', 'u'), ('r', 't', 't', 'u'), ('b', 'r', 't', 'u'), ('b', 'y', 'r', 't', 't', 'u'), ('y', 'r', 'u'), ('t', 'b', 'y', 'r', 'e', 't', 't', 'u'), ('t', 'y', 'r', 'e', 't', 't', 'u'), ('t', 'b', 'y', 't', 'u'), ('t', 't', 'u'), ('b', 'y', 'u'), ('t', 'r', 'u'), ('y', 'r', 't', 't', 'u'), ('t', 'b', 'y', 'r', 'e', 'u'), ('t', 'r', 'e', 'u'), ('r', 'e', 'u'), ('b', 'y', 'r', 't', 'u'), ('t', 'y', 'r', 'e', 't', 'u'), ('y', 't', 't', 'u'), ('b', 'e', 't', 'u'), ('t', 'b', 'y', 'r', 't', 'u'), ('r', 'e', 't', 't', 'u'), ('t', 'b', 'r', 'e', 'u'), ('t', 'e', 't', 't', 'u'), ('t', 'e', 'u'), ('b', 'y', 't', 't', 'u'), ('b', 'y', 'r', 'u'), ('t', 'b', 'r', 't', 'u'), ('t', 'b', 'r', 't', 't', 'u'), ('b', 'r', 'e', 't', 'u'), ('e', 't', 'u'), ('b', 'r', 'e', 'u'), ('t', 'y', 'u'), ('b', 'y', 't', 'u'), ('y', 'e', 't', 'u'), ('t', 'y', 'r', 'u'), ('t', 'r', 't', 'u'), ('t', 'e', 't', 'u'), ('t', 'b', 't', 't', 'u'), ('b', 'y', 'r', 'e', 't', 'u'), ('t', 'y', 'e', 'u'), ('r', 'e', 't', 'u'), ('t', 'y', 't', 'u'), ('t', 'b', 'e', 't', 'u'), ('t', 'b', 'y', 'r', 'e', 't', 'u'), ('t', 'b', 'r', 'u'), ('t', 'y', 'e', 't', 't', 'u'), ('b', 'y', 'e', 't', 't', 'u'), ('t', 'b', 'y', 'r', 'u'), ('e', 't', 't', 'u'), ('y', 'r', 'e', 't', 'u'), ('b', 'r', 'e', 't', 't', 'u'), ('b', 'e', 'u'), ('b', 't', 'u'), ('t', 'b', 'y', 'u'), ('t', 'b', 'y', 'e', 'u'), ('y', 't', 'u'), ('y', 'r', 't', 'u'), ('y', 'r', 'e', 'u'), ('t', 't', 't', 'u'), ('b', 'y', 'r', 'e', 't', 't', 'u'), ('t', 'r', 't', 't', 'u'), ('t', 'y', 'r', 't', 'u'), ('t', 'y', 'r', 't', 't', 'u'), ('b', 'y', 'e', 't', 'u'), ('t', 'b', 'y', 'e', 't', 't', 'u'), ('r', 't', 'u'), ('b', 'r', 'u'), ('t', 'r', 'e', 't', 't', 'u'), ('t', 'y', 'e', 't', 'u'), ('t', 'y', 't', 't', 'u'), ('t', 'b', 'e', 'u'), ('b', 'e', 't', 't', 'u'), ('b', 'r', 't', 't', 'u'), ('t', 'y', 'r', 'e', 'u'), ('t', 'b', 'y', 'e', 't', 'u'), ('t', 'b', 'y', 'r', 't', 't', 'u'), ('b', 't', 't', 'u'), ('t', 'b', 'r', 'e', 't', 't', 'u')}
        rack = 'tbyrett'
        placed_tile = 'u'
        stu_S = generate_combinations(rack,placed_tile)
        print("Instructor:",inst_S)
        print("Student   :",stu_S)
        assert inst_S == stu_S
        
        
    def test_generate_words(self):
    
        scrabble_words_dict = {'bat':1,'ate':1,'cat':1,'eat':1,'tea':1}
        combo = ('a','e','t')
        inst_S = {'ate','eat','tea'}
        stu_S = generate_words(combo,scrabble_words_dict)
        print("Combination:",combo)
        print("Instructor:",inst_S)
        print("Student   :",stu_S)
        assert inst_S == stu_S
        
    def test_generate_words_with_scores(self):

        scrabble_words_dict = {'baker':1,'success':1,'use':1,'sue':1,'other':1,'judgment':1,'menu':1}
        rack = 'judgent'
        placed_tile = 'm'
        inst_D = {'menu': 6, 'judgment': 69}
        stu_D = generate_words_with_scores(rack,placed_tile,scrabble_words_dict)
        print("rack,placed_tile:", rack, placed_tile)
        print("Instructor: ",inst_D)
        print("Student:    ",stu_D)
        assert inst_D == stu_D
        rack = 'uccesss'
        placed_tile = ''
        inst_D = {'sue': 3, 'use': 3, 'success': 61}
        stu_D = generate_words_with_scores(rack,placed_tile,scrabble_words_dict)
        print("rack,placed_tile:", rack, placed_tile)
        print("Instructor: ",inst_D)
        print("Student:    ",stu_D)
        assert inst_D == stu_D


        
    def test_read_file(self):
        
        inst_D = {'bat': 1, 'tire': 1, 'desire': 1, 'youth': 1}
        fp = open('tiny.txt')
        stu_D = read_file(fp)
        print("Instructor:",inst_D)
        print("Student   :",stu_D)
        assert inst_D == stu_D

    def test_sort_words(self):
    
        D = {'ear': 3, 'era': 3, 'screen': 8, 'since': 7, 'ice': 5, 'rise': 4, 'sea': 3, 'case': 6, 'raise': 5, 'arise': 5, 'earn': 4, 'near': 4, 'see': 3, 'race': 6, 'care': 6, 'increase': 60, 'ease': 4, 'rice': 6, 'nice': 6, 'scene': 7}
        print("Dictionary:",D)
        inst_score =  [('increase', 60, 8), ('screen', 8, 6), ('scene', 7, 5), ('since', 7, 5), ('care', 6, 4), ('case', 6, 4), ('nice', 6, 4), ('race', 6, 4), ('rice', 6, 4), ('arise', 5, 5), ('raise', 5, 5), ('ice', 5, 3), ('earn', 4, 4), ('ease', 4, 4), ('near', 4, 4), ('rise', 4, 4), ('ear', 3, 3), ('era', 3, 3), ('sea', 3, 3), ('see', 3, 3)]
        inst_len = [('increase', 60, 8), ('screen', 8, 6), ('scene', 7, 5), ('since', 7, 5), ('arise', 5, 5), ('raise', 5, 5), ('care', 6, 4), ('case', 6, 4), ('nice', 6, 4), ('race', 6, 4), ('rice', 6, 4), ('earn', 4, 4), ('ease', 4, 4), ('near', 4, 4), ('rise', 4, 4), ('ice', 5, 3), ('ear', 3, 3), ('era', 3, 3), ('sea', 3, 3), ('see', 3, 3)]
        stu_score,stu_len = sort_words(D)
        print("Instructor Score order:", inst_score)
        print("Instructor Length order:", inst_len)
        print("Student Score order    :", stu_score)
        print("Student Length order   :", stu_len)
        assert inst_score == stu_score and inst_len == stu_len
        
    def test_1(self):
    
        ### test cases done through Mimir with the input matching the expected output
        
        #input
        """y\ncommon_3000.txt\ntbyrett\ngulp\nn\n"""
        
        #excpected out put
        """Scrabble Tool
        Would you like to enter an example (y/n): Input word file: Input the rack (2-7chars): Input tiles on board (enter for none): Word choices sorted by Score
         Score  -  Word
            11  -  pretty
            10  -  buyer
             9  -  bury
             9  -  type
             8  -  butter
        Word choices sorted by Length
        Length  -  Word
             6  -  pretty
             6  -  butter
             5  -  buyer
             4  -  bury
             4  -  type
        Do you want to enter another example (y/n): Thank you for playing the game"""
        pass


    def test_2(self):
    
        ### test cases done through Mimir with the input matching the expected output

        #input
        """y
        common_3000.txt
        tbyrett

        n"""
        
        #expected output
        
        """Scrabble Tool
        Would you like to enter an example (y/n): Input word file: Input the rack (2-7chars): Input tiles on board (enter for none): Word choices sorted by Score
         Score  -  Word
             6  -  try
             6  -  yet
             5  -  bet
        Word choices sorted by Length
        Length  -  Word
             3  -  try
             3  -  yet
             3  -  bet
        Do you want to enter another example (y/n): Thank you for playing the game"""
        
        pass
        
        
    def test_3(self):
            
        ### test cases done through Mimir with the input matching the expected output

        #input
        """y
        common_3000.txt
        aabsti
        xya
        n"""
        
        #expected output
        
        """Scrabble Tool
        Would you like to enter an example (y/n): Input word file: Input the rack (2-7chars): Input tiles on board (enter for none): Word choices sorted by Score
         Score  -  Word
            10  -  six
            10  -  tax
             7  -  stay
             6  -  say
        Word choices sorted by Length
        Length  -  Word
             4  -  stay
             3  -  six
             3  -  tax
             3  -  say
        Do you want to enter another example (y/n): Thank you for playing the game
        """
        
        pass
        

    def test_4(self):
    
        ### test cases done through Mimir with the input matching the expected output

        #input
        """y
        common_3000.txt
        increas
        e
        y
        common_3000.txt
        uccesss

        n"""
        
        #expected output
        
        """Scrabble Tool
        `Would you like to enter an example (y/n): Input word file: Input the rack (2-7chars): Input tiles on board (enter for none): Word choices sorted by Score
         Score  -  Word
            60  -  increase
             8  -  screen
             7  -  scene
             7  -  since
             6  -  care
        Word choices sorted by Length
        Length  -  Word
             8  -  increase
             6  -  screen
             5  -  scene
             5  -  since
             5  -  arise
        Do you want to enter another example (y/n): Input word file: Input the rack (2-7chars): Input tiles on board (enter for none): Word choices sorted by Score
         Score  -  Word
            61  -  success
             3  -  sue
             3  -  use
        Word choices sorted by Length
        Length  -  Word
             7  -  success
             3  -  sue
             3  -  use
        Do you want to enter another example (y/n): Thank you for playing the game"""
            
        pass

if __name__ == "__main__":
    unittest.main()
