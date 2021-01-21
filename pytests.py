import numpy
import sys
test = {'kek': 'foo', 'lorem': 'ipsum'}
numpy.savetxt('test.txt', test, delimiter=" ", fmt="%s") 
