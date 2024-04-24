import tkinter as tk
from tkinter import ttk

def on_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

# Create a Tkinter window
root = tk.Tk()
root.title("Full-Screen Scrollbar Example")

# Create a Canvas widget
canvas = tk.Canvas(root)
canvas.pack(side="left", fill="both", expand=True)

# Add a Frame inside the Canvas
frame = ttk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor="nw")

# Configure the Canvas to resize with the window
canvas.bind("<Configure>", on_configure)

# Create a Text widget inside the Frame
text = tk.Text(frame, wrap="none")
text.pack(fill="both", expand=True)

# Create a vertical Scrollbar for the Canvas
vsb = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
vsb.pack(side="right", fill="y")
canvas.configure(yscrollcommand=vsb.set)

# Create a horizontal Scrollbar for the Canvas
hsb = ttk.Scrollbar(root, orient="horizontal", command=canvas.xview)
hsb.pack(side="bottom", fill="x")
canvas.configure(xscrollcommand=hsb.set)

# Add some content to the Text widget
for i in range(100):
    text.insert("end", f"Line {i+1}\n")

treeview = ttk.Treeview(frame)
treeview.pack(side="left", fill="both", expand=True)
# Run the Tkinter event loop
root.mainloop()
