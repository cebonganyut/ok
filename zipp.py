import zipfile
import os

def extract_zip():
    # Meminta input nama file ZIP dari pengguna
    zip_file_name = input("Masukkan nama file ZIP yang akan diekstrak: ")

    # Memeriksa apakah file ada
    if not os.path.exists(zip_file_name):
        print(f"Error: File '{zip_file_name}' tidak ditemukan.")
        return

    # Meminta input direktori tujuan ekstraksi
    extract_dir = input("Masukkan direktori tujuan ekstraksi (biarkan kosong untuk direktori saat ini): ")
    if not extract_dir:
        extract_dir = os.getcwd()

    try:
        with zipfile.ZipFile(zip_file_name, 'r') as zip_ref:
            # Mendapatkan daftar file dalam arsip ZIP
            file_list = zip_ref.namelist()
            
            print(f"File yang akan diekstrak:")
            for file in file_list:
                print(f"- {file}")
            
            # Konfirmasi ekstraksi
            confirm = input("Lanjutkan ekstraksi? (y/n): ").lower()
            if confirm != 'y':
                print("Ekstraksi dibatalkan.")
                return

            # Melakukan ekstraksi
            zip_ref.extractall(extract_dir)
            print(f"Ekstraksi selesai. File telah diekstrak ke: {extract_dir}")
    
    except zipfile.BadZipFile:
        print(f"Error: File '{zip_file_name}' bukan file ZIP yang valid.")
    except Exception as e:
        print(f"Terjadi kesalahan saat mengekstrak: {str(e)}")

if __name__ == "__main__":
    extract_zip()
