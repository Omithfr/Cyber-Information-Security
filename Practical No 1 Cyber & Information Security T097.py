print("T097 Omith")
####1A(CLI)
##def caesar_cipher(text, key, mode='e'):
##    result = ""
##    # If decrypting, we just shift backwards
##    if mode == 'd': 
##        key = -key
##        
##    for char in text:
##        if char.isalpha():
##            shift = 65 if char.isupper() else 97
##            result += chr((ord(char) - shift + key) % 26 + shift)
##        else:
##            result += char
##    return result
##
##def rail_fence_cipher(text, key, mode='e'):
##    if mode == 'e':
##        rail = [['\n' for _ in range(len(text))] for _ in range(key)]
##        dir_down = False
##        row, col = 0, 0
##        
##        for i in range(len(text)):
##            if (row == 0) or (row == key - 1):
##                dir_down = not dir_down
##            rail[row][col] = text[i]
##            col += 1
##            row += 1 if dir_down else -1
##            
##        return "".join([rail[i][j] for i in range(key) for j in range(len(text)) if rail[i][j] != '\n'])
##
##    elif mode == 'd':
##        rail = [['\n' for _ in range(len(text))] for _ in range(key)]
##        dir_down = None
##        row, col = 0, 0
##        
##        for i in range(len(text)):
##            if row == 0: dir_down = True
##            if row == key - 1: dir_down = False
##            rail[row][col] = '*'
##            col += 1
##            row += 1 if dir_down else -1
##            
##        index = 0
##        for i in range(key):
##            for j in range(len(text)):
##                if ((rail[i][j] == '*') and (index < len(text))):
##                    rail[i][j] = text[index]
##                    index += 1
##                    
##        result = []
##        row, col = 0, 0
##        for i in range(len(text)):
##            if row == 0: dir_down = True
##            if row == key - 1: dir_down = False
##            if rail[row][col] != '*':
##                result.append(rail[row][col])
##                col += 1
##            row += 1 if dir_down else -1
##        return "".join(result)
##
##def main():
##    print("👋 Welcome to the Secret Message Maker!")
##    
##    while True:
##        print("\nWhat kind of cipher do you want to use?")
##        print("  [1 or s] Substitution (Caesar)")
##        print("  [2 or t] Transposition (Rail Fence)")
##        print("  [q] Quit")
##        
##        choice = input("Your choice: ").strip().lower()
##        
##        if choice == 'q':
##            print("Catch you later! Stay secure. 🕵️‍♂️")
##            break
##            
##        if choice not in ['1', 's', '2', 't']:
##            print("Oops, I didn't recognize that choice. Let's try again.")
##            continue
##
##        text = input("\nWhat's your message? ")
##        
##        # Friendly error handling for the key
##        try:
##            key = int(input("Enter your secret key (a whole number): "))
##        except ValueError:
##            print("Hmm, that doesn't look like a number. Let's start over!")
##            continue
##
##        mode_input = input("Do you want to (e)ncrypt or (d)ecrypt? ").strip().lower()
##        
##        # Map 'encrypt' or 'e' to just 'e'
##        if mode_input.startswith('e'):
##            mode = 'e'
##            action_word = "Encrypted"
##        elif mode_input.startswith('d'):
##            mode = 'd'
##            action_word = "Decrypted"
##        else:
##            print("Please type 'e' or 'd'. Let's start over!")
##            continue
##
##        # Execute the chosen cipher
##        if choice in ['1', 's']:
##            output = caesar_cipher(text, key, mode)
##        else:
##            if key < 2:
##                print("For Rail Fence, the key needs to be 2 or higher!")
##                continue
##            output = rail_fence_cipher(text, key, mode)
##
##        print("-" * 30)
##        print(f"✨ Here is your {action_word} message:")
##        print(f"👉 {output}")
##        print("-" * 30)
##
##if __name__ == "__main__":
##    main()

'''1A(GUI)'''
import tkinter as tk
from tkinter import ttk, messagebox

# --- Core Cryptography Logic ---

def caesar_cipher(text, key, mode='e'):
    result = ""
    if mode == 'd': 
        key = -key
    for char in text:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result

def rail_fence_cipher(text, key, mode='e'):
    if mode == 'e':
        rail = [['\n' for _ in range(len(text))] for _ in range(key)]
        dir_down = False
        row, col = 0, 0
        for i in range(len(text)):
            if (row == 0) or (row == key - 1): dir_down = not dir_down
            rail[row][col] = text[i]
            col += 1
            row += 1 if dir_down else -1
        return "".join([rail[i][j] for i in range(key) for j in range(len(text)) if rail[i][j] != '\n'])
    
    elif mode == 'd':
        rail = [['\n' for _ in range(len(text))] for _ in range(key)]
        dir_down = None
        row, col = 0, 0
        for i in range(len(text)):
            if row == 0: dir_down = True
            if row == key - 1: dir_down = False
            rail[row][col] = '*'
            col += 1
            row += 1 if dir_down else -1
        index = 0
        for i in range(key):
            for j in range(len(text)):
                if rail[i][j] == '*' and index < len(text):
                    rail[i][j] = text[index]
                    index += 1
        result = []
        row, col = 0, 0
        for i in range(len(text)):
            if row == 0: dir_down = True
            if row == key - 1: dir_down = False
            if rail[row][col] != '*':
                result.append(rail[row][col])
                col += 1
            row += 1 if dir_down else -1
        return "".join(result)

# --- GUI Application Logic ---

def process_text():
    text = text_entry.get("1.0", "end-1c")
    if not text.strip():
        messagebox.showwarning("Empty Input", "Please enter a message to process.")
        return

    try:
        key = int(key_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Key", "Your secret key must be a whole number.")
        return

    mode = mode_var.get()
    cipher_type = cipher_var.get()

    if cipher_type == "s":
        output = caesar_cipher(text, key, mode)
    else:
        if key < 2:
            messagebox.showerror("Invalid Key", "Rail Fence requires a key of 2 or more.")
            return
        output = rail_fence_cipher(text, key, mode)

    # Animate output update
    output_entry.config(state="normal")
    output_entry.delete("1.0", "end")
    output_entry.insert("1.0", output)
    output_entry.config(state="disabled")

def copy_to_clipboard():
    output = output_entry.get("1.0", "end-1c")
    if output.strip():
        root.clipboard_clear()
        root.clipboard_append(output)
        messagebox.showinfo("Success", "Copied to clipboard! 📋")
    else:
        messagebox.showwarning("Empty", "Nothing to copy yet.")

def clear_all():
    text_entry.delete("1.0", "end")
    key_entry.delete(0, "end")
    output_entry.config(state="normal")
    output_entry.delete("1.0", "end")
    output_entry.config(state="disabled")

# --- UI Setup & Layout ---

# Define Colors for Dark Theme
BG_COLOR = "#1e1e2e"
FG_COLOR = "#cdd6f4"
ACCENT_COLOR = "#a6e3a1"
HOVER_COLOR = "#94cc90"
ENTRY_BG = "#313244"

root = tk.Tk()
root.title("Advanced Cryptography Tool")
root.geometry("550x680")
root.configure(bg=BG_COLOR)
root.resizable(False, False)

# Styling using ttk
style = ttk.Style()
style.theme_use('clam')

# Configure Radiobutton style for dark theme
style.configure("Dark.TRadiobutton", background=BG_COLOR, foreground=FG_COLOR, font=("Segoe UI", 10))
style.map("Dark.TRadiobutton",
          background=[('active', BG_COLOR)],
          indicatorcolor=[('selected', ACCENT_COLOR), ('!selected', ENTRY_BG)])

# Title Header
header = tk.Label(root, text="🛡️ Secret Message Maker", font=("Segoe UI", 18, "bold"), bg=BG_COLOR, fg=ACCENT_COLOR)
header.pack(pady=(20, 15))

# Main Container
frame = tk.Frame(root, bg=BG_COLOR)
frame.pack(padx=30, fill="both", expand=True)

# Message Input
tk.Label(frame, text="1. Enter Your Message:", font=("Segoe UI", 11, "bold"), bg=BG_COLOR, fg=FG_COLOR).pack(anchor="w")
text_entry = tk.Text(frame, height=4, font=("Consolas", 11), bg=ENTRY_BG, fg=FG_COLOR, insertbackground=FG_COLOR, relief="flat", padx=10, pady=10)
text_entry.pack(fill="x", pady=(5, 15))

# Key Input
tk.Label(frame, text="2. Secret Key (Integer):", font=("Segoe UI", 11, "bold"), bg=BG_COLOR, fg=FG_COLOR).pack(anchor="w")
key_entry = tk.Entry(frame, font=("Consolas", 12), bg=ENTRY_BG, fg=FG_COLOR, insertbackground=FG_COLOR, relief="flat")
key_entry.pack(fill="x", pady=(5, 15), ipady=5)

# Options Frame (Side-by-side Layout)
options_frame = tk.Frame(frame, bg=BG_COLOR)
options_frame.pack(fill="x", pady=10)

# Cipher Selection Column
cipher_frame = tk.Frame(options_frame, bg=BG_COLOR)
cipher_frame.pack(side="left", expand=True, fill="both")
tk.Label(cipher_frame, text="3. Choose Cipher:", font=("Segoe UI", 11, "bold"), bg=BG_COLOR, fg=FG_COLOR).pack(anchor="w", pady=(0, 5))

cipher_var = tk.StringVar(value="s")
ttk.Radiobutton(cipher_frame, text="Caesar (Substitution)", variable=cipher_var, value="s", style="Dark.TRadiobutton").pack(anchor="w", pady=2)
ttk.Radiobutton(cipher_frame, text="Rail Fence (Transposition)", variable=cipher_var, value="t", style="Dark.TRadiobutton").pack(anchor="w", pady=2)

# Mode Selection Column
mode_frame = tk.Frame(options_frame, bg=BG_COLOR)
mode_frame.pack(side="right", expand=True, fill="both")
tk.Label(mode_frame, text="4. Choose Action:", font=("Segoe UI", 11, "bold"), bg=BG_COLOR, fg=FG_COLOR).pack(anchor="w", pady=(0, 5))

mode_var = tk.StringVar(value="e")
ttk.Radiobutton(mode_frame, text="Encrypt Message", variable=mode_var, value="e", style="Dark.TRadiobutton").pack(anchor="w", pady=2)
ttk.Radiobutton(mode_frame, text="Decrypt Message", variable=mode_var, value="d", style="Dark.TRadiobutton").pack(anchor="w", pady=2)

# Buttons Frame
btn_frame = tk.Frame(frame, bg=BG_COLOR)
btn_frame.pack(fill="x", pady=20)

# Custom Hover Function for Main Button
def on_enter(e):
    magic_btn.config(bg=HOVER_COLOR)
def on_leave(e):
    magic_btn.config(bg=ACCENT_COLOR)

clear_btn = tk.Button(btn_frame, text="Clear All", command=clear_all, font=("Segoe UI", 10, "bold"), bg="#f38ba8", fg="#1e1e2e", relief="flat", cursor="hand2", padx=15, pady=8)
clear_btn.pack(side="left")

magic_btn = tk.Button(btn_frame, text="✨ Process Message", command=process_text, font=("Segoe UI", 12, "bold"), bg=ACCENT_COLOR, fg="#1e1e2e", relief="flat", cursor="hand2", padx=20, pady=8)
magic_btn.pack(side="right")
magic_btn.bind("<Enter>", on_enter)
magic_btn.bind("<Leave>", on_leave)

# Output Section
output_header = tk.Frame(frame, bg=BG_COLOR)
output_header.pack(fill="x")
tk.Label(output_header, text="Result:", font=("Segoe UI", 11, "bold"), bg=BG_COLOR, fg=FG_COLOR).pack(side="left")
tk.Button(output_header, text="📋 Copy", command=copy_to_clipboard, font=("Segoe UI", 8), bg=ENTRY_BG, fg=FG_COLOR, relief="flat", cursor="hand2").pack(side="right")

output_entry = tk.Text(frame, height=4, font=("Consolas", 12), bg=ENTRY_BG, fg=ACCENT_COLOR, relief="flat", padx=10, pady=10, state="disabled")
output_entry.pack(fill="x", pady=(5, 10))

# Start the application loop
if __name__ == "__main__":
    root.mainloop()
