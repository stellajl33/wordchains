path = 'small.txt'
startword = 'big'
endword = 'bag'

mydict = []

def match(s1, s2):
    num = 0
    if len(s1) != len(s2):
        return False
    else:
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                num += 1
        if num == 1:
        #print num, s1, s2
            print num
            return True
        else:
            #print num, s1, s2
            print num
            return False


def createdict(word):
    mydict = {word:[]}
    if len(word) == len(endword):
        with open(path,'r') as words:
            for line in words:
                if line != startword:
                    if match(line, word) == True:
                        mydict[word].append(line[:-1])
    return mydict


v = match('bad', 'bag')
b = match('bandicoot', 'bag')
print v
print b

createdict('big')
print mydict
