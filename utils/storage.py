import json
import os
from datetime import datetime

file_path = os.path.join("data", "notes.json")

def load_notes():
    if not os.path.exists("data"):
        os.makedirs("data")
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            json.dump([], f)
    with open(file_path, "r") as f:
        return json.load(f)

def save_notes(notes):
    with open(file_path, "w") as f:
        json.dump(notes, f, indent=4)

def save_note(content):
    notes = load_notes()
    note = {
        "id": str(len(notes) + 1),
        "content": content,
        "timestamp": datetime.now().isoformat()
    }
    notes.append(note)
    save_notes(notes)
    print("✅ Not eklendi.")

def list_notes():
    notes = load_notes()
    if not notes:
        print("📭 Hiç not yok.")
        return
    for note in notes:
        print(f"[{note['id']}] {note['content']} ({note['timestamp'][:10]})")

def delete_note(note_id):
    notes = load_notes()
    filtered = [n for n in notes if n["id"] != note_id]
    if len(filtered) == len(notes):
        print("❌ Not bulunamadı.")
    else:
        save_notes(filtered)
        print("🗑️ Not silindi.")

