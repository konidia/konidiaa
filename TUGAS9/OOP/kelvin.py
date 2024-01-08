class Kelvin:
    def __init__(self, suhu):
        self.suhu = suhu

    def get_kelvin(self):
        val = self.suhu
        return val

    def get_reamur(self):
        val = (4/5) * (self.suhu - 273.15)
        return val

    def get_fahrenheit(self):
        val = (9/5) * (self.suhu - 273.15) + 32
        return val

    def get_celsius(self):
        val = self.suhu - 273.15
        return val

# Input
suhu_kelvin = float(input("Masukkan suhu dalam Kelvin: "))
K = Kelvin(suhu_kelvin)
val = K.get_kelvin()

# Konversi ke Reamur
reamur = K.get_reamur()

# Konversi ke Fahrenheit
fahrenheit = K.get_fahrenheit()

# Konversi ke Celsius
celsius = K.get_celsius()

# Output
print(f"{val:.2f} Kelvin, sama dengan:")
print(f"{reamur:.2f} Reamur")
print(f"{fahrenheit:.2f} Fahrenheit")
print(f"{celsius:.2f} Celsius")
