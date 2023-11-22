import tkinter as tk
from tkinter import messagebox

def simpan_jadwal():
    # Ambil data dari input pengguna
    hari = hari_entry.get()
    waktu = waktu_entry.get()
    mata_kuliah = mata_kuliah_entry.get()

    if not hari or not waktu or not mata_kuliah:
        messagebox.showerror("Error", "Harap isi semua kolom.")
        return

    # Buka berkas untuk penulisan
    with open("jadwal_kuliah.txt", "a") as file:
        file.write(f"{hari}, {waktu}, {mata_kuliah}\n")

    # Bersihkan input
    hari_entry.delete(0, tk.END)
    waktu_entry.delete(0, tk.END)
    mata_kuliah_entry.delete(0, tk.END)

def tampilkan_jadwal():
    # Buka berkas untuk membaca dan tampilkan isinya
    with open("jadwal_kuliah.txt", "r") as file:
        jadwal = file.read()
        tampilkan_jadwal_label.config(text=jadwal)

# Membuat jendela utama
window = tk.Tk()
window.title("Jadwal Kuliah")

# Membuat elemen-elemen antarmuka pengguna
tk.Label(window, text="Hari:").pack()
hari_entry = tk.Entry(window)
hari_entry.pack()

tk.Label(window, text="Waktu:").pack()
waktu_entry = tk.Entry(window)
waktu_entry.pack()

tk.Label(window, text="Mata Kuliah:").pack()
mata_kuliah_entry = tk.Entry(window)
mata_kuliah_entry.pack()

simpan_button = tk.Button(window, text="Simpan Jadwal", command=simpan_jadwal)
simpan_button.pack()

tampilkan_jadwal_button = tk.Button(window, text="Tampilkan Jadwal", command=tampilkan_jadwal)
tampilkan_jadwal_button.pack()

tampilkan_jadwal_label = tk.Label(window, text="")
tampilkan_jadwal_label.pack()

# Mulai aplikasi
window.mainloop()
