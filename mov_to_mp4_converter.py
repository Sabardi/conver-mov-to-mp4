#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Program untuk mengkonversi file MOV ke MP4 secara batch
Author: Assistant
"""

import os
import sys
import subprocess
import argparse
from pathlib import Path
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('conversion.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

class MOVToMP4Converter:
    def __init__(self):
        self.supported_formats = ['.mov', '.MOV']
        self.output_format = '.mp4'
        
    def check_ffmpeg(self):
        """Cek apakah FFmpeg terinstall di sistem"""
        try:
            subprocess.run(['ffmpeg', '-version'], 
                         capture_output=True, check=True)
            logger.info("FFmpeg ditemukan di sistem")
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            logger.error("FFmpeg tidak ditemukan! Silakan install FFmpeg terlebih dahulu.")
            logger.error("Download dari: https://ffmpeg.org/download.html")
            return False
    
    def find_mov_files(self, folder_path):
        """Cari semua file MOV dalam folder"""
        folder = Path(folder_path)
        if not folder.exists():
            logger.error(f"Folder tidak ditemukan: {folder_path}")
            return []
        
        if not folder.is_dir():
            logger.error(f"Path bukan folder: {folder_path}")
            return []
        
        mov_files = []
        for file_path in folder.rglob('*'):
            if file_path.is_file() and file_path.suffix in self.supported_formats:
                mov_files.append(file_path)
        
        logger.info(f"Ditemukan {len(mov_files)} file MOV di folder: {folder_path}")
        return mov_files
    
    def convert_file(self, input_file, output_file):
        """Konversi file MOV ke MP4 menggunakan FFmpeg"""
        try:
            logger.info(f"Memulai konversi: {input_file.name}")
            
            # Command FFmpeg untuk konversi
            cmd = [
                'ffmpeg',
                '-i', str(input_file),           # Input file
                '-c:v', 'libx264',              # Video codec
                '-c:a', 'aac',                  # Audio codec
                '-preset', 'medium',             # Encoding speed
                '-crf', '23',                   # Quality (18-28, semakin rendah semakin bagus)
                '-y',                           # Overwrite output file
                str(output_file)                 # Output file
            ]
            
            # Jalankan FFmpeg
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                check=True
            )
            
            logger.info(f"Konversi berhasil: {input_file.name} -> {output_file.name}")
            return True
            
        except subprocess.CalledProcessError as e:
            logger.error(f"Error saat konversi {input_file.name}: {e.stderr}")
            return False
        except Exception as e:
            logger.error(f"Error tidak terduga saat konversi {input_file.name}: {str(e)}")
            return False
    
    def convert_folder(self, folder_path, create_subfolder=True):
        """Konversi semua file MOV dalam folder"""
        if not self.check_ffmpeg():
            return False
        
        mov_files = self.find_mov_files(folder_path)
        if not mov_files:
            logger.warning("Tidak ada file MOV ditemukan dalam folder")
            return True
        
        # Buat folder output jika diperlukan
        output_folder = Path(folder_path)
        if create_subfolder:
            output_folder = output_folder / "converted_mp4"
            output_folder.mkdir(exist_ok=True)
            logger.info(f"Folder output: {output_folder}")
        
        success_count = 0
        total_files = len(mov_files)
        
        logger.info(f"Memulai konversi {total_files} file...")
        
        for i, mov_file in enumerate(mov_files, 1):
            logger.info(f"Progress: {i}/{total_files}")
            
            # Buat nama file output
            output_file = output_folder / f"{mov_file.stem}{self.output_format}"
            
            # Konversi file
            if self.convert_file(mov_file, output_file):
                success_count += 1
        
        logger.info(f"Konversi selesai! {success_count}/{total_files} file berhasil dikonversi")
        return success_count == total_files

def main():
    parser = argparse.ArgumentParser(
        description="Konversi file MOV ke MP4 secara batch",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Contoh penggunaan:
  python mov_to_mp4_converter.py "C:\\Users\\User\\Videos"
  python mov_to_mp4_converter.py "D:\\Movies" --no-subfolder
        """
    )
    
    parser.add_argument(
        'folder_path',
        help='Path ke folder yang berisi file MOV'
    )
    
    parser.add_argument(
        '--no-subfolder',
        action='store_true',
        help='Simpan file hasil konversi di folder yang sama (default: buat subfolder)'
    )
    
    args = parser.parse_args()
    
    # Validasi input
    if not os.path.exists(args.folder_path):
        logger.error(f"Folder tidak ditemukan: {args.folder_path}")
        sys.exit(1)
    
    # Jalankan konversi
    converter = MOVToMP4Converter()
    success = converter.convert_folder(
        args.folder_path, 
        create_subfolder=not args.no_subfolder
    )
    
    if success:
        logger.info("Semua file berhasil dikonversi!")
        sys.exit(0)
    else:
        logger.error("Beberapa file gagal dikonversi. Cek log untuk detail.")
        sys.exit(1)

if __name__ == "__main__":
    main()

