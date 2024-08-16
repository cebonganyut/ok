import instaloader
import pandas as pd

# Inisialisasi instaloader
L = instaloader.Instaloader()

# Masukkan username target
target_username = input("Masukkan username Instagram target: ")

# Dapatkan profil target
profile = instaloader.Profile.from_username(L.context, target_username)

# Dapatkan followers dan followees
followers = set(profile.get_followers())
followees = set(profile.get_followees())

# Temukan yang belum follow balik
not_following_back = followees - followers

# Temukan mutual followers
mutual_followers = followers.intersection(followees)

# Buat DataFrame untuk hasil
df = pd.DataFrame({
    'Username': [user.username for user in not_following_back],
    'Status': 'Tidak Follow Balik'
})

# Tambahkan yang sudah follow balik
df = df.append(pd.DataFrame({
    'Username': [user.username for user in mutual_followers],
    'Status': 'Follow Balik'
}), ignore_index=True)

# Simpan hasil ke file CSV
df.to_csv(f'{target_username}_follower_status.csv', index=False)

print(f"Hasil telah disimpan ke {target_username}_follower_status.csv")
