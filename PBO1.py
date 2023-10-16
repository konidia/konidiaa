import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import math

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Kalkulator Bangun Datar")

        self.label = tk.Label(master, text="Pilih Bangun Datar:")
        self.label.pack(padx=100,pady=50)

        self.options = ["Persegi", "Persegi Panjang", "Segitiga", "Lingkaran", "Trapesium", "Layang-Layang", "Jajar Genjang", "Belah Ketupat"]
        self.selected_option = tk.StringVar()
        self.selected_option.set(self.options[0])

        self.option_menu = tk.OptionMenu(master, self.selected_option, *self.options)
        self.option_menu.pack(padx=100,pady=50)

        self.calculate_button = tk.Button(master, text="Hitung", command=self.calculate,bg="#0000ff")
        self.calculate_button.pack(padx=100,pady=50)

    def calculate(self):
        selected_shape = self.selected_option.get()

        if selected_shape == "Persegi":
            self.calculate_persegi()
        elif selected_shape == "Persegi Panjang":
            self.calculate_persegi_panjang()
        elif selected_shape == "Segitiga":
            self.calculate_segitiga()
        elif selected_shape == "Lingkaran":
            self.calculate_lingkaran()
        elif selected_shape == "Trapesium":
            self.calculate_trapesium()
        elif selected_shape == "Layang-Layang":
            self.calculate_layang_layang()
        elif selected_shape == "Jajar Genjang":
            self.calculate_jajar_genjang()
        elif selected_shape == "Belah Ketupat":
            self.calculate_belah_ketupat()
        else:
            messagebox.showinfo("Peringatan", "Pilih bangun datar yang valid.")

    def calculate_persegi(self):
        sisi = float(self.get_user_input("Masukkan panjang sisi:"))
        luas = sisi ** 2
        keliling = 4 * sisi
        self.show_result(luas, keliling)

    def calculate_persegi_panjang(self):
        panjang = float(self.get_user_input("Masukkan panjang:"))
        lebar = float(self.get_user_input("Masukkan lebar:"))
        luas = panjang * lebar
        keliling = 2 * (panjang + lebar)
        self.show_result(luas, keliling)

    def calculate_segitiga(self):
        alas = float(self.get_user_input("Masukkan panjang alas:"))
        tinggi = float(self.get_user_input("Masukkan tinggi:"))
        luas = 0.5 * alas * tinggi
        keliling = alas + 2 * (math.sqrt(alas * 2 + tinggi * 2))
        self.show_result(luas, keliling)

    def calculate_lingkaran(self):
        jari_jari = float(self.get_user_input("Masukkan jari-jari:"))
        luas = math.pi * jari_jari ** 2
        keliling = 2 * math.pi * jari_jari
        self.show_result(luas, keliling)

    def calculate_trapesium(self):
        sisi_a = float(self.get_user_input("Masukkan panjang sisi a:"))
        sisi_b = float(self.get_user_input("Masukkan panjang sisi b:"))
        tinggi = float(self.get_user_input("Masukkan tinggi:"))
        luas = 0.5 * (sisi_a + sisi_b) * tinggi
        keliling = sisi_a + sisi_b + 2 * (math.sqrt((tinggi * 2) + (((sisi_b - sisi_a) * 2) / 4)))
        self.show_result(luas, keliling)

    def calculate_layang_layang(self):
        diagonal1 = float(self.get_user_input("Masukkan panjang diagonal 1:"))
        diagonal2 = float(self.get_user_input("Masukkan panjang diagonal 2:"))
        luas = 0.5 * diagonal1 * diagonal2
        keliling = 2 * (math.sqrt((0.5 * diagonal1) * 2 + (0.5 * diagonal2) * 2))
        self.show_result(luas, keliling)

    def calculate_jajar_genjang(self):
        alas = float(self.get_user_input("Masukkan panjang alas:"))
        tinggi = float(self.get_user_input("Masukkan tinggi:"))
        luas = alas * tinggi
        keliling = 2 * (alas + tinggi)
        self.show_result(luas, keliling)

    def calculate_belah_ketupat(self):
        diagonal1 = float(self.get_user_input("Masukkan panjang diagonal 1:"))
        diagonal2 = float(self.get_user_input("Masukkan panjang diagonal 2:"))
        luas = 0.5 * diagonal1 * diagonal2
        keliling = 4 * (math.sqrt(0.5 * (diagonal1 * 2 + diagonal2 * 2)))
        self.show_result(luas, keliling)

    def get_user_input(self, message):
        return simpledialog.askfloat("Input", message)

    def show_result(self, luas, keliling):
        messagebox.showinfo("Hasil Perhitungan", f"Luas: {luas}\nKeliling: {keliling}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()