'''Go to terminal and then write your file path and then write python programme name.py and write your argument'''
'''cd.. , cd python'''
'''import statement is used for command line'''
'''for execution open terminal and then write python commandline.py "value" '''
'''python prog1.py vansh xyz abc in this statement here python will consider prog1.py as [0] argument and after that user input will consider as [1]'''

import sys
# name=sys.argv[1]
# print("\nvalue=",name)


'''print all command line inputs'''
print("Number Of Arguments:=",len(sys.argv))
print("\nThe Command Line Argument are:=")

for i in range(0,len(sys.argv)):
    print(sys.argv[i])