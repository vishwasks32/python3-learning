#!/usr/bin/env python3.6

#Author: Vishwas K Singh
#Email: vishwasks32@gmail.com
# Program: Sequence(String) Multiplication Example
#          Listing2.3

# Prints a sentence in a centered "box" of correct width

sentence = input("Sentence: ")
screen_width = 80
text_width   = len(sentence)
box_width    = text_width + 6
left_margin  = (screen_width - box_width) // 2

print()
print(' ' * left_margin + '+' + '-' * (box_width-2) +   '+')
print(' ' * left_margin + '| ' + ' ' * (text_width-2) + ' |')
print(' ' * left_margin + '| ' +        sentence      + ' |')
print(' ' * left_margin + '| ' + ' ' * (text_width-2) + ' |')
print(' ' * left_margin + '+' + '-' * (box_width-2) +   '+')
print()

