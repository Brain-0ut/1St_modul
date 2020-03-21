# coding: utf-8
def spam(number):    
    return 'bulochka'*number


def my_sum(list_of_numbers):
    x = 0
    for i in list_of_numbers:
        x += i
    return x


def shortener(string):
    s = string.split()
    l = [word if len(word)<=6 else str(word)[:6] +"*" for word in s]
    new_s = ' '.join(l)
    return new_s 


def compare_ends(words):
    i = 0
    for word in words:
        if len(word)>=2 and word[0] == word[-1]:
            i+=1
    return i