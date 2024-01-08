class Fahrenheit:
    def __init__(self, suhu):
        self.suhu = suhu

    def get_fahrenheit(self):
        val = self.suhu
        return val

    def get_celsius(self):
        val = (5/9) * (self.suhu - 32)
        return val

    def get_reamur(self):
        val = (4/9) * (self.suhu - 32)
        return val

    def get_kelvin(self):
        val = (5/9) * (self.suhu - 32) + 273.15
        return val

# Input
suhu_fahrenheit = float(input("Masukkan suhu dalam Fahrenheit: "))
F = Fahrenheit(suhu_fahrenheit)
val = F.get_fahrenheit()

# Konversi ke Celsius
celsius = F.get_celsius()

# Konversi ke Reamur
reamur = F.get_reamur()

# Konversi ke Kelvin
kelvin = F.get_kelvin()

# Output
print(f"{val:.2f} Fahrenheit, sama dengan:")
print(f"{celsius:.2f} Celsius")
print(f"{reamur:.2f} Reamur")
print(f"{kelvin:.2f} Kelvin")
