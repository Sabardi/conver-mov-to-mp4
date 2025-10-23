@echo off
chcp 65001 >nul
title MOV to MP4 Converter

echo ================================================
echo        MOV to MP4 Converter - Windows
echo ================================================
echo.

REM Cek apakah Python terinstall
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python tidak ditemukan!
    echo 💡 Silakan install Python terlebih dahulu dari https://python.org
    pause
    exit /b 1
)

REM Cek apakah file converter ada
if not exist "mov_to_mp4_converter.py" (
    echo ❌ File mov_to_mp4_converter.py tidak ditemukan!
    echo 💡 Pastikan file ada di folder yang sama dengan batch ini.
    pause
    exit /b 1
)

REM Jalankan converter
echo 🚀 Menjalankan MOV to MP4 Converter...
echo.
python mov_to_mp4_converter.py

echo.
echo ================================================
echo Konversi selesai! Tekan tombol apapun untuk keluar.
pause >nul
