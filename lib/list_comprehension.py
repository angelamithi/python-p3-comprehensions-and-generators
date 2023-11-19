#!/usr/bin/env python3

def return_evens(num_list):
    even_numbers=[num for num in num_list if num % 2 == 0]
    return even_numbers
    
numbers_even=return_evens([0, 1, 3, 5, 7, 8, 9])
print (numbers_even)



def make_exclamation(sentence_list):
    sentence_with_exclamation=[word + "!" for word in sentence_list ]
    return sentence_with_exclamation
sentence=make_exclamation(["Hello", "I'm doing great", "Python is fun"])
print (sentence)