import tkinter as tk

root = tk.Tk()
root.title("Greeting")
root.geometry("300x150")

tk.Label(root, text="Hi Ivan", font=("Arial", 24)).pack(expand=True)

root.mainloop()
