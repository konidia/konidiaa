class Reamur:
    def __init__(self, suhu):
        self.suhu = suhu

    def get_reamur(self):
        val = self.suhu
        return val

    def get_celsius(self):
        val = (5/4) * self.suhu
        return val

    def get_fahrenheit(self):
        val = (9/4) * self.suhu + 32
        return val

    def get_kelvin(self):
        val = (5/4) * self.suhu + 273.15
        return val

# Input
suhu_reamur = float(input("Masukkan suhu dalam Reamur: "))
R = Reamur(suhu_reamur)
val = R.get_reamur()

# Konversi ke Celsius
celsius = R.get_celsius()

# Konversi ke Fahrenheit
fahrenheit = R.get_fahrenheit()

# Konversi ke Kelvin
kelvin = R.get_kelvin()

# Output
print(f"{val:.2f} Reamur, sama dengan:")
print(f"{celsius:.2f} Celsius")
print(f"{fahrenheit:.2f} Fahrenheit")
print(f"{kelvin:.2f} Kelvin")
