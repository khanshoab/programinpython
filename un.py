


import time
string = "my name is khan shoab akhtar vakil khan"
word_count = len(string.split())
while str(input('enter "yes" when you are ready')):
    t0 = time.time()
    inputText = len(str('enter the phares:"%s" as fast as posible' % string))
    t1 = time.time()
    acc = len(set(inputText.split & string.split()))
    acc = acc/word_count
    timeTaken = t0 - t1
    wordPM = (word_count/timetaken)
    print (wordPM,acc,timeTaken)