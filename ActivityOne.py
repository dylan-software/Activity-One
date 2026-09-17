import tkinter as tk


def build_ui():
    window = tk.Tk()
    window.geometry("420x360")
    window.title("Activity One")

    result = tk.Label(window, text="Result: ")
    result.pack(pady=5)

    # 1
    list_a = ["Coconut", "Watermelon", "Apple", "Cherry", "Strawberry"]
    list_b = [
        ["Minecraft", "Terraria", "Pac-Man"],
        ["Hollow Knight", "Celeste", "Doom"],
        ["The Forest", "Raft", "Subnautica"],
    ]

    # 2
    tk.Label(window, text="List_1 (1x5)", font=("Arial", 10, "bold")).pack(pady=5)
    interactive_box_a = []
    frame_a = tk.Frame(window)
    frame_a.pack(pady=5)

    for i, value in enumerate(list_a):
        entry = tk.Entry(frame_a, width=10)
        entry.grid(row=0, column=i, padx=2)
        entry.insert(0, value)
        interactive_box_a.append(entry)

    tk.Label(window, text="List_2 (3x3)", font=("Arial", 10, "bold")).pack(pady=5)
    interactive_box_b = []
    frame_b = tk.Frame(window)
    frame_b.pack(pady=5)

    for f, row_values in enumerate(list_b):
        row_box = []
        for c, value in enumerate(row_values):
            entry = tk.Entry(frame_b, width=10)
            entry.grid(row=f, column=c, padx=2, pady=2)
            entry.insert(0, value)
            row_box.append(entry)
        interactive_box_b.append(row_box)

    # 3
    def save_data():
        try:
            saved_list_a = [e.get() for e in interactive_box_a]
            saved_list_b = [[e.get() for e in row] for row in interactive_box_b]
            result.config(text=f"list_create:\nA: {saved_list_a}\nB: {saved_list_b}")
        except Exception:
            result.config(text="mistake")

    button_save = tk.Button(window, text="save and show list", command=save_data, bg="lightgreen")
    button_save.pack(pady=10)

    return window


if __name__ == "__main__":
    window = build_ui()
    window.mainloop()
