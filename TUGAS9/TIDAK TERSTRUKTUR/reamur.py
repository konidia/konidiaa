print("Konversi Suhu Reamur")

# Entry
suhu = input("Masukkan suhu dalam Reamur:")

# Rumus
C = 5/4 * float(suhu)
F = (9/4 * float(suhu)) + 32
K = 5/4 * float(suhu) + 273

# Output
print(suhu + " Reamur sama dengan ")
print(str(C) + " Celcius")
print(str(F) + " Fahrenheit")
print(str(K) + " Kelvin")

# Nama, NIM dan Kelas
print("\nNama: Rama Hardiansyah")
print("NIM: 220511075")
print("Kelas: TIF22C / R3")