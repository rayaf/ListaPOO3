class TV:

    def __init__(self):
        self.volume = 0
        self.setCanal(0)

    def setCanal(self, canal):
        if (canal >= 0) and (canal <= 100):
            self.canal = canal

    def volumeUp(self):
        if (self.volume < 100):
            self.volume += 1

    def volumeDown(self):
        if (self.volume > 0):
            self.volume -= 1

tv = TV()
tv.setCanal(10)
tv.volumeUp()
tv.volumeUp()
tv.volumeUp()
tv.volumeDown()
tv.setCanal(12)
print("Canal: %d - Volume: %d" % (tv.canal, tv.volume))
