# TO demo our own iter on letters...

class MyIterator:

    def __init__(self, letters):
        """
        Constructor
        """
        self.letters = letters
        self.position = 0

    def __iter__(self):
        """
        Returns itself as an iterator
        """
        return self

    def __next__(self):
        """
        Returns the next letter in the sequence or 
        raises StopIteration
        """
        if self.position >= len(self.letters):
            raise StopIteration
        letter = self.letters[self.position]
        self.position += 1
        return letter

if __name__ == '__main__':

    i = MyIterator('abcd')
    for item in i:
        print(item)

    i = MyIterator([(1,2),(2,3),(3,4)])
    for item in i:
        print(item)
