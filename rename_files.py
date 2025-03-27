import os
import tkinter as tk
from tkinter import filedialog, messagebox

class FileRenamerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Renamer")
        self.root.geometry("400x300")
        
        # Variables
        self.directory = tk.StringVar()
        self.base_name = tk.StringVar(value="yash")
        self.id_value = tk.StringVar(value="0")
        
        # GUI Elements
        tk.Label(root, text="File Renamer", font=("Arial", 14)).pack(pady=10)
        
        tk.Label(root, text="Directory:").pack()
        tk.Entry(root, textvariable=self.directory, width=40).pack()
        tk.Button(root, text="Browse", command=self.browse_directory).pack(pady=5)
        
        tk.Label(root, text="Base Name:").pack()
        tk.Entry(root, textvariable=self.base_name, width=20).pack(pady=5)
        
        tk.Label(root, text="ID Number:").pack()
        id_options = ["0", "1", "2", "3", "4", "5"]  # You can extend this list
        tk.OptionMenu(root, self.id_value, *id_options).pack(pady=5)
        
        tk.Button(root, text="Rename Files", command=self.rename_files).pack(pady=20)
    
    def browse_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.directory.set(directory)
    
    def rename_files(self):
        directory = self.directory.get()
        base_name = self.base_name.get()
        id_num = self.id_value.get()
        
        if not directory or not base_name or not id_num:
            messagebox.showerror("Error", "Please specify directory, base name, and ID")
            return
        
        try:
            files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
            files.sort()
            counter = 1
            
            for filename in files:
                file_ext = os.path.splitext(filename)[1]
                # New format: base_name + id + . + series_number
                new_filename = f"{base_name}{id_num}.{counter}{file_ext}"
                
                old_path = os.path.join(directory, filename)
                new_path = os.path.join(directory, new_filename)
                
                os.rename(old_path, new_path)
                counter += 1
            
            messagebox.showinfo("Success", f"Renamed {counter-1} files successfully!\n"
                              f"Format: {base_name}{id_num}.[1-{counter-1}]")
            
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FileRenamerApp(root)
    root.mainloop()