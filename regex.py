import re

random_text = '''
My name is Mr. Neo. My phone number is 123-456-7890. My email is ChosenOne@gmail.com
My name is Mr. Morphius. My phone number is 413-234-2568. My email is CoolGuy@yahoo.com. 
My name is Mrs. Trinity. My phone number is 285-036-8215. My email is ChosenOnesGirl1@apple.com.
'''

re.findall("@([a-z]+)", random_text)