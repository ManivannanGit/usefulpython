import pprint
# demonstrate exploration of data structure
# we have a recursive relationship, 
# here given by a nested dict just begging to be recursed.
master = {0: {1: {'a': {'apple': {}, 'apricot': {}}, 'b': {}},
              2: {'paper': {}, 'rock': {}, 'scissors': {}}}}

# we'll create a method to flatten it:
def flatten(d):
    l = []
    def flat(e):
        for key, value in e.iteritems():
            l.append(key)
            flat(value)
    flat(d)
    return l


l = flatten(master)
pprint.pprint(l)
# returns [0, 1, 2, 'a', 'b', 'apricot', 'apple', 'scissors', 'paper', 'rock']
# And create a method to provide a flat dict pointing to a tuple of each node's parent key and it's flattened hierarchy

def restructure(d):
    r = {}
    top = d.keys()[0]
    r[top] = (None, frozenset(flatten(d)))
    def recurse(e):
        for parent, hierarchy in e.iteritems():
            for node, child in hierarchy.iteritems():
                all = flatten(child)
                all.append(node)
                # data structure here
                r[node] = (parent, frozenset(all))
            recurse(hierarchy)
    recurse(d)
    return r

easyview = restructure(master)
pprint.pprint(easyview)

## Now the hard part: reconstruct the master data structure from 
## the "easy view" restructured version.

def reconstruct(d):
    ''' expect d[node] = (parent, hlist) '''
    cache = {}
    # get all children with no children
    for node, (parent, hlist) in d.items():
        if len(hlist) == 1:
            cache.setdefault(parent, {})
            cache[parent].update({node: {}})
            d.pop(node)
    pprint.pprint(cache)
    # need step to integrate bottom children if necessary
    for node in cache.keys():
        parent = d.get(node, ['NA'])[0]
        print 'parent is ', parent
        if parent in cache:
            cache[parent].update({node: cache.pop(node, {})})
    # assemble with rest of children
    whileloops = 0
    while d:
        whileloops += 1
        for node, (parent, hlist) in d.items(): 
            if node in cache:
                print 'node: {node}, parent: {parent}'.format(node=node, parent=parent)
                if parent is not None:
                    cache.setdefault(parent, {})
                    cache[parent].update({node: cache.pop(node, {})})
                    d.pop(node)
                else: 
                    cache.update({node: cache.pop(node, {})})
                    d.pop(node)
        if whileloops > 1000:
            break
    print 'while loops: ', whileloops
    return cache

easyview = restructure(master)
reconstructed = reconstruct(easyview)
print reconstructed == master
pprint.pprint(reconstructed)
pprint.pprint(master)
