import tkinter as tk

window = tk.Tk()
window.geometry("300x300")
window.title("Activity One")

result = tk.Label(window, text="Result: ")
result.pack(pady=5)
# 1
list_a = ["Coconut", "Watermelon", "Apple", "Cherry", "Strawberry"]

list_b = [["Minecraft", "Terraria", "Pac-Man"],
          ["Hollow Knigth", "Celeste", "Doom"],
          ["The forest", "Raft", "Subnautica"]
]
# 2
tk.Label(window, text="List_1 (1x5)", font=("Arial", 10, "bold")).pack(pady=5)

interactive_box_a = []
frame_a = tk.Frame(window)
frame_a.pack(pady=5)

for i in range(5):
    entry = tk.Entry(frame_a, width=8)
    entry.grid(row=0, column=i, padx=2)
    interactive_box_a.append(entry)

tk.Label(window, text="List_2 (3x3)", font=("Arial", 10, "bold")).pack(pady=5)

interactive_box_b = []
frame_b = tk.Frame(window)
frame_b.pack(pady=5)

for f in range(3):
    row_box = []
    for c in range(3):
        entry = tk.Entry(frame_b, width=8)
        entry.grid(row=f, column=c, padx=2, pady=2)
        row_box.append(entry)
    interactive_box_b.append(row_box)


# 3
def save_data():
    try:
        list_a = [e.get() for e in interactive_box_a]
        list_b = [[e.get() for e in row] for row in interactive_box_b]
        result.config(text=f"list_create:\nA: {list_a}\nB: {list_b}")
    except Exception as e:
        result.config(text="mistake")
button_save = tk.Button(window, text="save and show list", command=save_data, bg="lightgreen")
button_save.pack(pady=10)



window.mainloop()

