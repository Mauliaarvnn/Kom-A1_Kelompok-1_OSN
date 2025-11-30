import pandas as pd

print("🔍 Membaca file 1NF...")
df = pd.read_excel("DATA_OSN_1NF_FIXED.xlsx")

print("🧠 Membuat tabel-tabel 2NF...")

# --- TABEL SEKOLAH ---
tabel_sekolah = df[[
    "Sekolah",
    "Jenjang Sekolah",
    "Provinsi",
    "Kab/Kota"
]].drop_duplicates().reset_index(drop=True)
tabel_sekolah.insert(0, "id_sekolah", range(1, len(tabel_sekolah) + 1))

# --- TABEL PESERTA ---
tabel_peserta = df.merge(tabel_sekolah, on=["Sekolah", "Jenjang Sekolah", "Provinsi", "Kab/Kota"], how="left")
tabel_peserta = tabel_peserta[[
    "id_peserta",
    "Nama Peserta",
    "Gender",
    "Kelas",
    "id_sekolah"
]].drop_duplicates().reset_index(drop=True)

# --- TABEL KOMPETISI ---
tabel_kompetisi = df[[
    "Bidang",
    "Jenjang Lomba",
    "Tahun"
]].drop_duplicates().reset_index(drop=True)
tabel_kompetisi.insert(0, "id_kompetisi", range(1, len(tabel_kompetisi) + 1))

# --- TABEL HASIL (Relasi Peserta–Kompetisi) ---
tabel_hasil = df.merge(tabel_kompetisi, on=["Bidang", "Jenjang Lomba", "Tahun"], how="left")
tabel_hasil = tabel_hasil[[
    "id_peserta",
    "id_kompetisi",
    "Medali",
    "Prize Tambahan"
]].reset_index(drop=True)
tabel_hasil.insert(0, "id_hasil", range(1, len(tabel_hasil) + 1))

print("💾 Menyimpan hasil ke file Excel...")
with pd.ExcelWriter("DATA_OSN_2NF_FIXED.xlsx", engine="openpyxl") as writer:
    tabel_peserta.to_excel(writer, sheet_name="Peserta", index=False)
    tabel_sekolah.to_excel(writer, sheet_name="Sekolah", index=False)
    tabel_kompetisi.to_excel(writer, sheet_name="Kompetisi", index=False)
    tabel_hasil.to_excel(writer, sheet_name="Hasil", index=False)

print("\n🎉 Normalisasi 2NF versi lengkap selesai!")
print("📁 File disimpan sebagai: DATA_OSN_2NF_FIXED.xlsx")
print("🧩 Ada 4 sheet di dalamnya: Peserta, Sekolah, Kompetisi, dan Hasil 💖")
