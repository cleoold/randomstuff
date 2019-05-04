# -*- coding:utf-8 -*-
# Fancy spam message displayer (C) cos in May 2019
# displays many messages and does not stop (must launch this in Linux, Mac or Android, iOS, Windows is not good in this)
import random as ran
import sys, time

class spamMsg:
    CHARSAMPLES = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'x', 'y', 'z',
                   '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    CHARSAMPLESEXT = ['py', 'py', 'py', 'py', 'll', 'll', 'll', 'deb', 'json']
    PROGRESSLOADED = ['#', '|', 'H', 'X', '█']
    PROGRESSNOTLOADED = ['-', '=', ' ', '_']
    #COLOURFULRATE = [0, 0, 0, 0, 0, 0, 0, 1]
    COLOURS = [32, 33, 34, 36, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37,
               37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37]
    # printNums() prints decimal integers in rows. Integers are random from [start] to [end]
    # [times] is how many times to repeat (in line)
    #   printNums: Int Int Int -> None
    def printNums(self, start, end, times):
        for _j in range(times):
            sys.stdout.flush()
            toPrint = ran.randint(start, end)
            print('\033[1;%dm %d \033[0m' % (ran.choice(spamMsg.COLOURS), toPrint), end = ' ')
            time.sleep(ran.uniform(0.05, 0.1))
        print()
    # printChar() prints a number and a random sequence of characters
    #   printChar: None -> None
    def printChar(self):
        print(ran.randint(1000, 9999), 
        ''.join(ran.sample(spamMsg.CHARSAMPLES, ran.randint(3, 20))))
    class spamFile:
        # getaFile() returns a random file name
        # getaFile: None -> Str
        def getaFile(self):
            return (''.join(ran.sample(spamMsg.CHARSAMPLES, ran.randint(3, 9))) + '.' + 
             ran.choice(spamMsg.CHARSAMPLESEXT))
        # printFileValue(current, total) prints spam file analysis. [total] and [current] are random
        # printFileValue: Int Int -> None
        def printFileValue(self, current, total): #| [total] is not used here
            fileName = spamMsg().spamFile().getaFile()                                           #|      
            print('Analysing file No.%d \033[1;%dm %s \033[0m'                                   #|
             % (current, ran.choice(spamMsg.COLOURS), fileName), end ='')                        #|
            if ran.choice([0, 0, 0, 0, 0, 0, 1]): #| true or false is random                     #|
                print('\n The file %s is either removed or corrupted. It is skipped.' % fileName)#| spam message
            else:                                                                                #|
                print(' . . . OK.')
        # printFileKey() prints spam file and key analysis. [length] is the length of the key string
        # [total] and [current] are random
        # printFileKey: Int -> None
        def printFileKey(self, length, current, total): #| [total] is not used here
            fileName = spamMsg().spamFile().getaFile()
            print('*** The file No.%d \033[1;%dm %s \033[0m is parsed with KEY \033[0;33m%s\033[0m.' 
             % (current, ran.choice(spamMsg.COLOURS), fileName, 
             str.upper(''.join(ran.sample(spamMsg.CHARSAMPLES, length)))))
    # printKey(length) prints a spam key, [length] is the length of each segment
    #   printKey: Int -> None
    def printKey(self, length):
        print('ANALYSED SECRET KEY: ', end = '')
        myRange = ran.randint(5, 10)
        for j in range(myRange):
            for _k in range(length):
                sys.stdout.flush()
                print(str.upper(ran.choice(spamMsg.CHARSAMPLES)), end = '')
                time.sleep(0.05)
            if j < myRange - 1: print(end = '-')
        print()
    class spamBar:
        # [width] is the width of bar, 
        # [count] is the current step count, [total] is the total steps, [style] is the chars of the bar
        # STYLE: [Str Str] example ['#', '-']
        def __init__(self, width = 10, total = 0, count = 0, style = ['#', '-']):
            self.width = width
            self.total = total
            self.count = count
            self.style = style
       # spamProgressOneLine(f) displays a spam progress bar, [f] is the procedure to 
       # operate during the spaming
       #   spamProgressOneLine: self (Int Int -> None) -> None
        def spamProgressOneLine(self, f):
           sys.stdout.write(' ' * (self.width + 20) + '\r') # 20 overwrites previous spaces
           sys.stdout.flush()
           f(self.count, self.total) #| function f uses two params which are current count and total count
           progress = self.width * self.count // self.total
           sys.stdout.write('%d/%d: ' % (self.count, self.total))
           sys.stdout.write(self.style[0] * progress + self.style[1] * (self.width - progress) + 
            ' (%.1f%%)' % (self.count / self.total * 100) + '\r')
           if progress == self.width: sys.stdout.write('\n')
           sys.stdout.flush()
        # spamProgress(f, timeLimit) displays them n a row
        # [timeLimit] is the lower and upper limit of random time eg [0.01, 0.5]
        #   spamProgressOneLine: self (Int Int -> None) [Float Float] -> None
        def spamProgress(self, f, timeLimit):
           for _j in range(self.total):
               self.count += 1
               self.spamProgressOneLine(f)
               time.sleep(ran.uniform(timeLimit[0], timeLimit[1]))
        # spamDots(amount) prints [width] [dot]s one by one. [dot] is first of [style]
        #   spamDots: self -> None
        def spamDots(self): # only uses [width] and [style]
            for _j in range(self.width):
                sys.stdout.flush()
                print(self.style[0], end = ' ')
                time.sleep(0.5)
            print()
    # spamTree() prints a spam list tree, [start] and [end] indicate range of repeating times
    # [length] is the max length of each line, [beginStr] is the string to print at the beginning
    #   spamTree: Int Int Int Str -> None
    def spamTree(self, start, end, length, beginStr):
        if end < 10: return
        for _j in range(start, end):
            sys.stdout.flush()
            print(beginStr, end = '')
            print('|', end = '')
            if ran.choice([0, 0, 1]):
                print('-' * ran.randint(5, length) + '\033[1;%dm %s \033[0m' 
                 % (ran.choice(spamMsg.COLOURS), spamMsg().spamFile().getaFile()))
                if ran.choice([0, 0, 1]):
                    spamMsg().spamTree(start, end // 2, length // 2, '|' + ' ' * ran.randint(5, length // 3))
            else: print()
            time.sleep(0.005) # the behavior of this procedure is undefined because it may repeat unknown times


# main() displays garbage spam messages
#   main: None -> None
#   effect: prints many lines; does not stop
def main():
    spam = spamMsg()
    print('\nHello world!\n     ♚\n')
    nthRun = 1
    while not time.sleep(0.3):
        print('Retrieving secret catalogs %d...' % nthRun)
        for j in range(ran.randint(3, 10)):
            spam.printNums(10, 99, ran.randint(5, 15))
            if j % 3 == 0: spam.printChar()                          #|
            if j % ran.randint(1, 10): spam.printNums(100, 9999, 1)  #| make random
            spam.spamBar(ran.randint(10, 20), ran.randint(5, 10), 0, 
             [ran.choice(spam.PROGRESSLOADED),                #|lambda: does nothing
              ran.choice(spam.PROGRESSNOTLOADED)]).spamProgress(lambda x, y: x, [0.01, 0.05])
        for _j in range(ran.randint(1, 5)): spam.printKey(ran.randint(4, 6))
        spam.spamBar(5, style = [' ◆ ']).spamDots()

        print('\nKEYS ANALYSING COMPLETE.\n\n\033[1;33;44mAnalyzing files...\033[0m')
        for _j in range(3): spam.spamBar(5, style = [' ◇ ']).spamDots()
        spam.spamBar(60, ran.randint(10, 400), 0, ['#', '_']).spamProgress(spam.spamFile().printFileValue, [0.01, 0.1])

        print('\nBUILD SYSTEM FILE.')
        spam.spamBar(5, style = [' ● ']).spamDots()
        spam.spamTree(20, 150, 70, '')
        print('\nDISPLAYED SYSTEM FILE.')
        spam.spamBar(5, style = [' ◆ ']).spamDots()

        spam.spamBar(50, ran.randint(10, 400), 0, ['#', '_']).spamProgress(
         lambda x, y: spam.spamFile().printFileKey(8, x, y), [0.01, 0.1]) #| lambda: curry, does nothing
        print('\nInterpreted and switched files %d.\n \033[1;36;43mSUCCESS.\033[0m\n' % nthRun)
        time.sleep(0.5)
        nthRun += 1

main()