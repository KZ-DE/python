class celcius:
    def __init__(self, temperatur: int = 0) -> None:
        self.temperatur: int = temperatur

    def convertToFarenheit(self) -> int | float:
        return (self.temperatur * 1.8) + 32


bejo = celcius()
bejo.temperatur = 37

print(f"suhu bejo dalam celcius = {bejo.temperatur}")
print(f"suhu bejo dalam farenheit = {bejo.convertToFarenheit()}")
print(f"cek tipe data variabel : {bejo.__dict__}")
