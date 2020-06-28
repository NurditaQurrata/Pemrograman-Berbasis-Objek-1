class Hero(object):
    __jumlah = 0
    def __init__(self, nama, jenis, kuat, serang, tahan):
        # semua property dalam bentuk private
        self.__nama = nama
        self.__jenis = jenis
        self.__kuat = kuat
        self.__serang = serang
        self.__tahan = tahan
        Hero.__jumlah += 1

    # method getter
    def getNama(self):
        return self.__nama

    def getJenis(self):
        return self.__jenis

    def getKuat(self):
        return self.__kuat

    def getSerang(self):
        return self.__serang

    def getTahan(self):
        return self.__tahan

    # method setter
    def setNama(self, nama):
        self.__nama = nama

    def setJenis(self, jenis):
        self.__jenis = jenis

    def setKuat(self, kuat):
        self.__kuat = kuat

    def setSerang(self, serang):
        self.__serang = serang

    def setTahan(self, tahan):
        self.__tahan = tahan


semar = Hero("Semar", "Hulubalang", 100, 15, 5)
cepot = Hero("Cepot", "Prajurit", 100, 8, 3)

print(semar.getNama())
print(semar.getKuat())
semar.setKuat(90)
print(semar.getKuat())
