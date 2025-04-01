#Input with paramters

import sys 

print(" Jenkins Build Using Parameters ! ")

X_VALUE = int(sys.argv[1])

Y_VALUE = int(sys.argv[2])

print(" Multiply = ", (X_VALUE * Y_VALUE))