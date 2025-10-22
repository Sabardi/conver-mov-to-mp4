# MOV to MP4 Converter

Program Python untuk mengkonversi file dengan ekstensi `.mov` ke `.mp4` secara batch dari folder yang Anda tentukan.

## Fitur

- ✅ Konversi batch semua file MOV dalam folder
- ✅ Mencari file MOV secara rekursif dalam subfolder
- ✅ Logging detail untuk monitoring proses
- ✅ Progress indicator
- ✅ Error handling yang baik
- ✅ Opsi untuk menyimpan hasil di folder terpisah atau folder yang sama

## Persyaratan

### Software yang Diperlukan

1. **Python 3.6 atau lebih baru**
2. **FFmpeg** - Harus terinstall di sistem

### Install FFmpeg

#### Windows
- Download dari [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)
- Atau gunakan Chocolatey: `choco install ffmpeg`

#### macOS
```bash
brew install ffmpeg
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install ffmpeg
```

#### Linux (CentOS/RHEL)
```bash
sudo yum install ffmpeg
```

## Cara Penggunaan

### 1. Basic Usage
```bash
python mov_to_mp4_converter.py "C:\Users\YourName\Videos"
```

### 2. Simpan hasil di folder yang sama (tanpa subfolder)
```bash
python mov_to_mp4_converter.py "D:\Movies" --no-subfolder
```

### 3. Contoh dengan path yang berbeda
```bash
# Windows
python mov_to_mp4_converter.py "E:\Tools\conver mov to mp4"

# macOS/Linux
python mov_to_mp4_converter.py "/Users/username/Videos"
```

## Cara Kerja Program

1. **Validasi**: Program akan mengecek apakah FFmpeg terinstall
2. **Scan Folder**: Mencari semua file dengan ekstensi `.mov` atau `.MOV`
3. **Konversi**: Menggunakan FFmpeg untuk mengkonversi setiap file ke MP4
4. **Output**: File hasil disimpan di folder `converted_mp4` (atau folder yang sama jika menggunakan `--no-subfolder`)

## Parameter FFmpeg yang Digunakan

- **Video Codec**: `libx264` (H.264)
- **Audio Codec**: `aac`
- **Preset**: `medium` (balance antara kecepatan dan ukuran file)
- **Quality**: `CRF 23` (kualitas bagus dengan ukuran file yang reasonable)

## Logging

Program akan membuat file log `conversion.log` yang berisi:
- Detail proses konversi
- Error messages jika ada
- Progress information

## Contoh Output

```
2024-01-15 10:30:15 - INFO - FFmpeg ditemukan di sistem
2024-01-15 10:30:15 - INFO - Ditemukan 5 file MOV di folder: C:\Users\Videos
2024-01-15 10:30:15 - INFO - Folder output: C:\Users\Videos\converted_mp4
2024-01-15 10:30:15 - INFO - Memulai konversi 5 file...
2024-01-15 10:30:15 - INFO - Progress: 1/5
2024-01-15 10:30:15 - INFO - Memulai konversi: video1.mov
2024-01-15 10:30:45 - INFO - Konversi berhasil: video1.mov -> video1.mp4
...
2024-01-15 10:32:30 - INFO - Konversi selesai! 5/5 file berhasil dikonversi
```

## Troubleshooting

### Error: "FFmpeg tidak ditemukan"
- Pastikan FFmpeg sudah terinstall
- Pastikan FFmpeg ada di PATH sistem
- Restart command prompt/terminal setelah install FFmpeg

### Error: "Folder tidak ditemukan"
- Pastikan path folder benar
- Gunakan tanda kutip jika path mengandung spasi
- Pastikan folder ada dan dapat diakses

### Konversi gagal untuk file tertentu
- Cek file log untuk detail error
- Pastikan file MOV tidak corrupt
- Pastikan ada ruang disk yang cukup

## Tips Penggunaan

1. **Backup Data**: Selalu backup file original sebelum konversi batch
2. **Ruang Disk**: Pastikan ada ruang disk yang cukup untuk file hasil
3. **Kualitas**: Jika ingin kualitas lebih tinggi, edit parameter `crf` di kode (nilai lebih rendah = kualitas lebih tinggi)
4. **Kecepatan**: Jika ingin konversi lebih cepat, ubah `preset` dari `medium` ke `fast`

## Lisensi

Program ini dibuat untuk keperluan personal dan edukasi. Silakan modifikasi sesuai kebutuhan Anda.

