import itertools

class WordCounter: 
        def __init__(self, file=None, words=None):
            self.file = file or 'text.txt'
            self.wordsAmount = words or 10
        
        def findFile(self):
            try: 
                file = open('text.txt', 'r')
                return file
            
            except:
                print('Error al leer el archivo')

        def wordAverage(self):
            wordsCounter = {}
            for line in self.findFile(): 
                line.rstrip()
                arrayLine = line.split(" ")
                for x in arrayLine:
                    if x in wordsCounter:
                        # print('Esta el elemento')
                        value = wordsCounter.get(x)
                        wordsCounter.update({x: value+1})
                    else:
                        wordsCounter.update({x: 1})
            wordsCounter = dict(sorted(wordsCounter.items(), key=lambda item: item[1], reverse=True))
            return print(dict(itertools.islice(wordsCounter.items(), self.wordsAmount)))

word = WordCounter(None, 2)
word.wordAverage()