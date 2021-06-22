import random
def initialize_caps_list():
    for i in char_list_small:
        char_list_caps.append(i.capitalize())
def len_checker(pwd):
    if len(pwd)>=16:
        print("Strong Password by length")
    else:
        print("Weak Password, You can use either of the password")
        print(password_generator())
        print(password_generator())
        print(password_generator())
        print(password_generator())
def random_symbol():
    symbol=random.choice(special_char)
    return symbol
def random_4digit():
    digit_4=random.randint(1000,9999)
    return digit_4
def random_3digit():
    digit_3=random.randint(100,999)
    return digit_3
def random_char_small():
    char_small=random.choice(char_list_small)
    return char_small
def random_char_caps():
    char_caps=random.choice(char_list_caps)
    return char_caps
special_char=["~","`","!","@","#","$","%","^","&","*","(",")","-","_","+","=",
        "{","}","[","]","|",",'"',"'","<",">",",".","?"]
char_list_small=["a", "b", "c", "d", "e", "f", "g", "h",
         "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

char_list_caps=[]
initialize_caps_list()
def password_generator():
    pass_symbol1=random_symbol()
    pass_symbol2=random_symbol()
    pass_symbol3=random_symbol()
    pass_digit_4=random_4digit()
    pass_digit_4_1=random_4digit()
    pass_digit_3=random_3digit()
    pass_small_char=random_char_small()
    pass_caps_char=random_char_caps()
    password_generated=str(pass_symbol1)+str(pass_symbol2)+str(pass_symbol3)+str(pass_digit_4)+str(pass_digit_4_1)+str(pass_digit_3)+pass_small_char+pass_caps_char
    return password_generated
def str_analyzer(str_2_b_checked):
    dig=0
    sc=0
    c_small=0
    c_caps=0

    for i in str_2_b_checked:
        if i.isdigit():
            dig+=1
        if i in special_char:
            sc=sc+1
        if i in char_list_small:
            c_small=c_small+1
        if i in char_list_caps:
            c_caps=c_caps+1
            
    print("Digits in Password are :  ",dig)
    print("Special Character are  :  ",sc)
    print("Caps Letters are       :  ",c_caps)
    print("Lower case letters are :  ",c_small)
    print("Total characters found :  ",len(str_2_b_checked))
    if dig>=7 and sc>=3 and c_caps>=1 and c_small>=1:
        print("Strong password")
    else:
        print("Weak Password")

str_pass=input("Enter a password:   ")
len_checker(str_pass)
str_analyzer(str_pass)