import tkinter as tk
import webbrowser

def search_all_platforms(query):
    platforms = [
        f"https://www.google.com/search?q={query}",
        f"https://www.youtube.com/results?search_query={query}",
        f"https://www.instagram.com/{query}",
        f"https://www.facebook.com/{query}"
    ]

    for url in platforms:
        webbrowser.open(url)

def handle_command(event=None):
    command = entry.get().strip()
    if command:
        search_all_platforms(command)

root = tk.Tk()
root.title("Multiplatform Search Automation")
root.geometry("400x150")
root.configure(bg="white")

tk.Label(
    root,
    text="Enter the keyword to search",
    bg="black",
    fg="white"
).pack(pady=10)

entry = tk.Entry(root, width=30)
entry.pack(pady=10)
entry.bind("<Return>", handle_command)

tk.Button(
    root,
    text="Search",
    command=handle_command
).pack(pady=5)

root.mainloop()
