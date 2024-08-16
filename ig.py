import instaloader
from collections import defaultdict

# Inisialisasi instaloader
L = instaloader.Instaloader()

# Masukkan username target
target_username = input("Masukkan username Instagram target: ")

# Dapatkan profil target
profile = instaloader.Profile.from_username(L.context, target_username)

# Dapatkan followers dan followees
followers = set(profile.get_followers())
followees = set(profile.get_followees())

# Temukan yang belum follow balik dan mutual followers
not_following_back = followees - followers
mutual_followers = followers.intersection(followees)

# Buat dictionary untuk menyimpan hasil
result = defaultdict(list)

for user in not_following_back:
    result["Tidak Follow Balik"].append(user.username)

for user in mutual_followers:
    result["Follow Balik"].append(user.username)

# Simpan hasil ke file txt
with open(f'{target_username}_follower_status.txt', 'w') as f:
    for status, usernames in result.items():
        f.write(f"{status}:\n")
        for username in usernames:
            f.write(f"- {username}\n")
        f.write("\n")

print(f"Hasil telah disimpan ke {target_username}_follower_status.txt")
