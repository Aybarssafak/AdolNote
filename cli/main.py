#!/usr/bin/env python3

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import argparse
from utils.storage import save_note, list_notes, delete_note

parser = argparse.ArgumentParser(description="AdolNote - Basit Not Alma Uygulaması")

parser.add_argument("--add", help="Yeni not ekle")
parser.add_argument("--list", action="store_true", help="Tüm notları listele")
parser.add_argument("--delete", help="Notu sil (ID gir)")

args = parser.parse_args()

if args.add:
    save_note(args.add)
elif args.list:
    list_notes()
elif args.delete:
    delete_note(args.delete)
else:
    print("Kullanım: --add, --list veya --delete seçeneklerinden birini kullan.")
