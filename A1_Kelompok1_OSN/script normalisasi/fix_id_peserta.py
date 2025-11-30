import pandas as pd

print("🔍 Membaca file DATA_OSN_1NF.xlsx ...")
df = pd.read_excel("DATA_OSN_1NF.xlsx")

print("🧠 Menambahkan kolom ID_Peserta unik...")
df.insert(0, "id_peserta", range(1, len(df) + 1))

print("💾 Menyimpan hasil ke file baru...")
df.to_excel("DATA_OSN_1NF_FIXED.xlsx", index=False)

print("\n🎉 Selesai beb!")
print("📁 File disimpan sebagai: DATA_OSN_1NF_FIXED.xlsx")
print("📄 Sekarang kamu punya kolom id_peserta yang bisa jadi Primary Key ❤️")
