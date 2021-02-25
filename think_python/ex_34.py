#!/usr/bin/env python3
# Author: Vishwas K Singh
# Email: vishwasks32@gmail.com
# Script to print a pattern
#     +----+----+
#     |    |    |
#     |    |    |
#     |    |    |
#     |    |    |
#     +----+----+
#     |    |    |
#     |    |    |
#     |    |    |
#     |    |    |
#     +----+----+
#
def print_pattern():
    print('+','-'*4,'+','-'*4,'+','-'*4,'+','-'*4,'+')
    for i in range(4):
        print('|',' '*4,'|',' '*4,'|',' '*4,'|',' '*4,'|')
    
    print('+','-'*4,'+','-'*4,'+','-'*4,'+','-'*4,'+')
    for i in range(4):
        print('|',' '*4,'|',' '*4,'|',' '*4,'|',' '*4,'|')
    
    print('+','-'*4,'+','-'*4,'+','-'*4,'+','-'*4,'+')

if __name__ == '__main__':
    for j in range(2):
        print_pattern()
