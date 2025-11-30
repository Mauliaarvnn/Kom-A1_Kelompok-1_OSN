import pandas as pd

print("🔍 Membaca data 1NF (hasil sebelumnya)...")

# Baca file hasil normalisasi 1NF kamu
df = pd.read_excel("DATA_OSN_1NF_FIXED.xlsx")

# --- CEK KOLOM ---
print("\n🧠 Kolom yang terbaca:")
print(df.columns.tolist())

# === TABEL PESERTA ===
peserta = df[["id_peserta", "Nama Peserta", "Gender", "Kelas"]].drop_duplicates().reset_index(drop=True)

# === TABEL SEKOLAH ===
sekolah = df[["Sekolah", "Jenjang Sekolah", "Provinsi", "Kab/Kota"]].drop_duplicates().reset_index(drop=True)
sekolah["id_sekolah"] = range(1, len(sekolah) + 1)

# === TABEL KOMPETISI ===
kompetisi = df[["Bidang", "Jenjang Lomba", "Tahun"]].drop_duplicates().reset_index(drop=True)
kompetisi["id_kompetisi"] = range(1, len(kompetisi) + 1)

# === TABEL HASIL ===
# Kita merge biar setiap peserta, sekolah, kompetisi bisa dihubungkan
hasil = df.merge(sekolah, on=["Sekolah", "Jenjang Sekolah", "Provinsi", "Kab/Kota"], how="left")
hasil = hasil.merge(kompetisi, on=["Bidang", "Jenjang Lomba", "Tahun"], how="left")
hasil = hasil[["id_peserta", "id_sekolah", "id_kompetisi", "Medali", "Prize Tambahan"]].drop_duplicates().reset_index(drop=True)

# === SIMPAN HASIL ===
with pd.ExcelWriter("DATA_OSN_3NF.xlsx") as writer:
    peserta.to_excel(writer, sheet_name="Peserta", index=False)
    sekolah.to_excel(writer, sheet_name="Sekolah", index=False)
    kompetisi.to_excel(writer, sheet_name="Kompetisi", index=False)
    hasil.to_excel(writer, sheet_name="Hasil", index=False)

print("\n✅ Normalisasi 3NF selesai!")
print("📁 File disimpan sebagai: DATA_OSN_3NF.xlsx")
