import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tkinter as tk
from tkinter import messagebox
from utils.storage import load_notes, save_note, delete_note

class AdolNoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AdolNote")
        self.root.geometry("450x500")
        self.root.configure(bg="#f0f0f0")
        
        # Üst giriş alanı
        top_frame = tk.Frame(root, bg="#f0f0f0")
        top_frame.pack(pady=10)
        
        # Custom Entry Canvas
        self.entry_canvas = tk.Canvas(top_frame, width=240, height=25, bg="white", highlightthickness=1, highlightcolor="#cccccc")
        self.entry_canvas.pack(side=tk.LEFT, padx=5)
        
        # Entry widget canvas içinde
        self.entry = tk.Entry(self.entry_canvas, border=0, highlightthickness=0, bg="white")
        self.entry_canvas.create_window(5, 12, anchor="w", window=self.entry, width=210)
        
        # X işareti (başlangıçta gizli)
        self.clear_x = None
        self.clear_circle = None
        
        # Entry olayları
        self.entry.bind('<KeyRelease>', self.on_entry_change)
        self.entry.bind('<FocusIn>', self.on_entry_focus_in)
        self.entry.bind('<FocusOut>', self.on_entry_focus_out)
        self.entry_canvas.bind('<Button-1>', self.on_canvas_click)
        
        tk.Button(top_frame, text="➕ Ekle", width=8, command=self.add_note).pack(side=tk.LEFT, padx=2)
        tk.Button(top_frame, text="🔄 Yenile", width=8, command=self.load_notes_gui).pack(side=tk.LEFT, padx=2)
        
        # Liste alanı
        self.notes_frame = tk.Frame(root, bg="#f0f0f0")
        self.notes_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.load_notes_gui()
    
    def on_entry_change(self, event=None):
        """Entry içeriği değiştiğinde X işaretini göster/gizle"""
        if self.entry.get().strip():
            self.show_clear_button()
        else:
            self.hide_clear_button()
    
    def on_entry_focus_in(self, event=None):
        """Entry'ye odaklanıldığında border rengini değiştir"""
        self.entry_canvas.config(highlightcolor="#4CAF50")
        self.on_entry_change()
    
    def on_entry_focus_out(self, event=None):
        """Entry'den çıkıldığında border rengini normale döndür"""
        self.entry_canvas.config(highlightcolor="#cccccc")
    
    def on_canvas_click(self, event):
        """Canvas'a tıklandığında"""
        # X butonuna tıklanıp tıklanmadığını kontrol et (16x16 piksel alan)
        center_x, center_y = 227, 12.5
        radius = 8
        if (self.clear_x and 
            event.x >= center_x - radius and event.x <= center_x + radius and 
            event.y >= center_y - radius and event.y <= center_y + radius):
            self.clear_entry()
        else:
            # Entry'ye odaklan
            self.entry.focus_set()
    
    def show_clear_button(self):
        """X işaretini göster"""
        if not self.clear_x:
            # Mükemmel daire arka plan (16x16 piksel)
            center_x, center_y = 227, 12.5
            radius = 8
            self.clear_circle = self.entry_canvas.create_oval(
                center_x - radius, center_y - radius, 
                center_x + radius, center_y + radius,
                fill="#f5f5f5", outline="#d0d0d0", width=1
            )
            # X işareti
            self.clear_x = self.entry_canvas.create_text(center_x, center_y, text="✕", 
                                                       font=("Arial", 9, "bold"), fill="#888888")
    
    def hide_clear_button(self):
        """X işaretini gizle"""
        if self.clear_x:
            self.entry_canvas.delete(self.clear_x)
            self.entry_canvas.delete(self.clear_circle)
            self.clear_x = None
            self.clear_circle = None
    
    def clear_entry(self):
        """Entry'yi temizle"""
        self.entry.delete(0, tk.END)
        self.hide_clear_button()
        self.entry.focus_set()
    
    def load_notes_gui(self):
        for widget in self.notes_frame.winfo_children():
            widget.destroy()

        notes = load_notes()
        if not notes:
            tk.Label(self.notes_frame, text="Hiç not yok.", bg="#f0f0f0").pack()
            return

        for i, note in enumerate(notes):
            frame = tk.Frame(self.notes_frame, bg="#ffffff", pady=3)
            frame.pack(fill=tk.X, padx=5, pady=2)
            frame.columnconfigure(1, weight=1)  # Orta sütun esnek

            # Kopyalandı mesajı
            copied_label = tk.Label(frame, text="✅ Kopyalandı", fg="green", bg="#ffffff")
            copied_label.grid(row=0, column=2, padx=5)
            copied_label.grid_remove()  # Başlangıçta gizli

            # Sil butonu
            del_btn = tk.Button(frame, text="🗑️", command=lambda nid=note['id']: self.delete_note_gui(nid), bg="#ffdddd")
            del_btn.grid(row=0, column=3, padx=5)

            # Not metni (esnek, ama sağdakileri itmez)
            label = tk.Label(
                frame,
                text=f"{note['content']} ({note['timestamp'][:10]})",
                anchor="w",
                bg="#ffffff",
                cursor="hand2",
                wraplength=380,
                justify="left"
            )
            label.grid(row=0, column=1, sticky="ew", padx=(5, 0))

            # Kopyalama
            label.bind("<Button-1>", lambda e, text=note['content'], cl=copied_label: self.copy_to_clipboard(text, cl))
        
    def add_note(self):
        content = self.entry.get().strip()
        if content:
            save_note(content)
            self.entry.delete(0, tk.END)
            self.hide_clear_button()
            self.load_notes_gui()
        else:
            messagebox.showwarning("Uyarı", "Lütfen boş not girmeyin.")
    
    def delete_note_gui(self, note_id):
        delete_note(note_id)
        self.load_notes_gui()
    
    def copy_to_clipboard(self, text, copied_label):
        self.root.clipboard_clear()
        self.root.clipboard_append(text)
        self.root.update()
        
        copied_label.grid()  # Tekrar göster (grid ile)
        copied_label.after(3000, lambda: copied_label.grid_remove())  # 3 sn sonra gizle
            


if __name__ == "__main__":
    root = tk.Tk()
    app = AdolNoteApp(root)
    root.mainloop()