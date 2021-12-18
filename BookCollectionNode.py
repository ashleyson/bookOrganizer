from Book import Book
class BookCollectionNode:
    def __init__(self, data):
        self.data = data
        self.next = None 

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newNext):
        self.next = newNext

    
