#Input with paramters

import sys 

print(" Jenkins Build Using Parameters ! ")

X_VALUE = int(sys.argv[0])

Y_VALUE = int(sys.argv[1])

print(" Multiply = ", (X_VALUE * Y_VALUE))