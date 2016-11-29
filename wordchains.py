#word chains

path = 'large.txt'

startword = raw_input("Insert start word: ")
endword = raw_input("Insert end word: ")

#put text file in list
with open(path,'r') as words:
    mydictlist = []
    for line in words:
        mydictlist.append(line[:-1])

#check if input words are in the textfile
if startword not in mydictlist:
    print "Startword is not in list. Try again."
    quit()

if endword not in mydictlist:
    print "Endword is not in list. Try again."
    quit()

startwordnum = list(startword)
endwordnum = list(endword)

#stop script if length doesn't match
if len(startwordnum) != len(endwordnum):
    print "Length of startword and endword does not equal. Try again."
    quit()

count = len(startword)

#mydict = {startword:[]}

#wordchains
queue = []
queue.append(startword)

#function that checks for letter matching
def match(s1, s2):
    num = 0
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            num += 1
    if num == 1:
    #print num, s1, s2
        return True
    else:
        #print num, s1, s2
        return False

#function to create first dictionary
def createdict(word):
    mydict = {word:[]}
    if len(word) == len(endword):
        with open(path,'r') as words:
            for line in words:
                if line != startword:
                    if len(line[:-1]) == len(startword):
                        if match(line, word) == True:
                            mydict[word].append(line[:-1])
    return mydict


currentword = startword
#print 'currentword', currentword
stack = []
searched = []

status = False
while status == False:
    currentdict = createdict(currentword)
    #print 'currentdict:', currentdict
    if endword in currentdict.keys():
        status = True
        searched.append(currentword)
        break
    else:
        searched.append(currentword)
        #print currentword
        #stack += currentdict[currentword]
        #print 1, currentdict[currentword]
        for w in currentdict[currentword]:
            if w not in searched:
                if w not in stack:
                    stack.append(w)
        boolean1 = False
        while boolean1 == False:
            for i in stack:
                if match(i, currentword) == True:
                    boolean1 = True
                    if i not in searched:
                        currentword = i
                        del stack[stack.index(i)]
                        break
            else:
                currentword = searched[-2]
                del searched[-1]
        #currentword = stack[-1]
        #print 'currentword:',currentword
        #print 'stack:',stack
        #print 'searched', searched


print 'searched final',searched

#print mydict
