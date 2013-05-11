
# Functions I wish there was a __builtin__ for:
containsall = lambda sentence, *words: all(word in sentence for word in words) if words
# e.g.:
>>> containsall('alpha beta', 'alph', 'pha b', 'beta')
True
>>> containsall('alpha beta', 'aleph', 'beta')
False

containsany = lambda sentence, *words: any(word in sentence for word in words) if words
# e.g.:
>>> containsany('alpha beta', 'alpha', 'eta')
True
>>> containsany('alpha beta', 'aleph', 'a beta')
True
>>> containsany('alpha beta', 'alfa', 'zeta')
False


# Math Functions that I probably shouldn't rewrite:
factorial = lambda x: reduce(lambda y, z: y*z, (i or 1 for i in xrange(x+1)))
# e.g. (0!, 1!, 5!):
>>> factorial(0)
1
>>> factorial(1)
1
>>> factorial(5) # 1*2*3*4*5
120



