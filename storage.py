import db_handler


class Storage():
    def __init__(self, maples = 0, kruegerrand = 0, philharmoniker = 0, kangaroo = 0):
        db_handler.createDB()
        self.mapleLeafAmount = maples
        self.kruegerrandAmount = kruegerrand
        self.philharmonikerAmount = philharmoniker
        self.kangarooAmount = kangaroo
        self.lastMaple = []
        self.lastKrueger = []
        self.lastPhil = []
        self.lastKangaroo = []
        self.lastKangaroo, self.lastKrueger, self.lastMaple, self.lastPhil = self.loadOld()
        self.lastUpdate = ""
        self.loadStorage()

    def saveStorage(self):
        treasure_querry = (f"INSERT INTO userData(kruegAmount, philAmount, mapleAmount, kangAmount) VALUES ({self.kruegerrandAmount},"
                                                         f"{self.philharmonikerAmount},"
                                                         f"{self.mapleLeafAmount},"
                                                         f"{self.kangarooAmount})")
        # print(treasure_querry)
        db_handler.saveData(treasure_querry)

    # Load latest Entry from userData
    def loadStorage(self):
        treasure_querry = ("SELECT * FROM userData WHERE entryID= (SELECT MAX(entryID) FROM userData)")
        chest = db_handler.getData(treasure_querry)
        if len(chest) > 0:
            chest = chest[0]
            self.kruegerrandAmount = chest[1]
            self.philharmonikerAmount = chest[2]
            self.mapleLeafAmount = chest[3]
            self.kangarooAmount = chest[4]

    def loadOld(self):
        kangaroo = None
        krueger = None
        maple = None
        phil = None
        # query = "SELECT * FROM priceHistory"

        return kangaroo, krueger, maple, phil