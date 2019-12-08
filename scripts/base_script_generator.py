#!/usr/bin/env python3
#
# Author: Vishwas K Singh
# Email: vishwasks32@gmail.com
#
# Script to generate skeleton python script files for programming

def scpgen(flename,author,email,desc):
    f = open(fname,"w")
    print("#!/usr/bin/env python3",file=f)
    print("#",file=f)
    print("# Author: "+author,file=f)
    print("# Email: "+email,file=f)
    print("#",file=f)
    print("# Script to "+desc,file=f)
    f.close()

if __name__ == "__main__":
    fname = input("Please Enter the file name: ")
    author = input("Please Enter the Author: ")
    email = input("Please Enter the Author Email: ")
    desc = input("Please Enter the Script Description: ")
    scpgen(fname,author,email,desc)
    print("File created successfully!!")

