import db_handler


class Storage():
    def __init__(self, maples = 0, kruegerrand = 0, philharmoniker = 0, kangaroo = 0):
        self.mapleLeafAmount = maples
        self.kruegerrandAmount = kruegerrand
        self.philharmonikerAmount = philharmoniker
        self.kangaroo = kangaroo
        self.lastMaple = []
        self.lastKrueger = []
        self.lastPhil = []
        self.lastKangaroo = []
        self.lastKangaroo, self.lastKrueger, self.lastMaple, self.lastPhil = self.loadOld()
        self.lastUpdate = ""

    def saveStorage(self):
        pass
        #db_handler.saveData()

    def loadStorage(self):
        pass

    def loadOld(self):
        kangaroo = None
        krueger = None
        maple = None
        phil = None
        query = "SELECT * FROM priceHistory"

        return kangaroo, krueger, maple, phil