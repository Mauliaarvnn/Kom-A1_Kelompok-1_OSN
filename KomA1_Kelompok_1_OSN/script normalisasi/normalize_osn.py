import pandas as pd

print("🔍 Membaca data dari Excel...")

# Baca file Excel tanpa header
df_raw = pd.read_excel("DATA OSN.xlsx", sheet_name=0, header=None)

# Temukan baris header yang berisi "Nama Peserta"
header_row = df_raw[df_raw.astype(str).apply(lambda r: r.str.contains("Nama Peserta", case=False, na=False)).any(axis=1)].index[0]
df_raw.columns = df_raw.iloc[header_row]
df = df_raw.drop(range(header_row + 1)).reset_index(drop=True)

# Hapus kolom kosong
df = df.loc[:, ~df.columns.isna()]

print("\n🧠 Kolom yang terdeteksi:")
for col in df.columns:
    print("-", col)

# Normalisasi kolom Prize Tambahan biar atomik
if "Prize Tambahan" in df.columns:
    df["Prize Tambahan"] = df["Prize Tambahan"].fillna("").astype(str)
    df = df.assign(**{
        "Prize Tambahan": df["Prize Tambahan"].str.split(",")
    }).explode("Prize Tambahan")
    df["Prize Tambahan"] = df["Prize Tambahan"].str.strip()

# Hapus baris kosong total
df = df.dropna(how="all")

# Simpan ke file baru
df.to_excel("DATA_OSN_1NF.xlsx", index=False)
print("\n✅ Normalisasi 1NF selesai!")
print("📁 File disimpan sebagai: DATA_OSN_1NF.xlsx")
