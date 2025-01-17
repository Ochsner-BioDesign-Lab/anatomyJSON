import json
import tkinter as tk
from tkinter import ttk
import requests

# Load JSON data from URL
github_url = "https://raw.githubusercontent.com/ColinCurtis/anatomyJSON/refs/heads/main/anatomical_parts.json"

# Fetch the JSON data
response = requests.get(github_url)

# Check if the request was successful
if response.status_code == 200:
    anatomical_data = response.json()  # Parse the JSON into a Python dictionary
    print("Successfully loaded JSON data!")
else:
    print(f"Failed to fetch JSON. Status code: {response.status_code}")
    anatomical_data = {}

# Alternatively, load JSON data from file
"""
with open("anatomical_parts.json", "r") as file:
    anatomical_data = json.load(file)
"""

class AnatomyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Anatomy Search Tool")

        # Frame for the search and combobox
        self.left_frame = ttk.Frame(root)
        self.left_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Frame for the anatomy details
        self.right_frame = ttk.Frame(root)
        self.right_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        # Search input
        ttk.Label(self.left_frame, text="Search Input:").grid(row=0, column=0, sticky="w")
        self.search_input = ttk.Entry(self.left_frame, width=30)
        self.search_input.grid(row=1, column=0, sticky="w")
        self.search_input.bind("<KeyRelease>", self.search_anatomy)

        # Combobox for anatomical parts
        ttk.Label(self.left_frame, text="Select Anatomy:").grid(row=2, column=0, sticky="w")
        self.combobox = ttk.Combobox(self.left_frame, state="readonly", width=30)
        self.combobox['values'] = list(anatomical_data.keys())
        self.combobox.bind("<<ComboboxSelected>>", self.display_anatomy_details)
        self.combobox.grid(row=3, column=0, columnspan=2, sticky="w")

        # Text widget to display anatomy details
        self.details_text = tk.Text(self.right_frame, width=50, height=25, wrap="word")
        self.details_text.grid(row=0, column=0, sticky="nsew")

    def search_anatomy(self, event=None):
        input_text = self.search_input.get().strip().lower()
        matches = []

        for anatomy, details in anatomical_data.items():
            keywords = details.get("keywords", [])
            exclude_keywords = details.get("exclude_keywords", [])

            if any(keyword in input_text for keyword in keywords) and not any(kw in input_text for kw in exclude_keywords):
                matches.append(anatomy)

        self.details_text.delete(1.0, tk.END)

        if matches:
            self.details_text.insert(tk.END, "Matched Anatomies:\n\n")
            for match in matches:
                details = anatomical_data.get(match, {})
                self.details_text.insert(tk.END, f"Anatomy: {match}\n")
                self.details_text.insert(tk.END, json.dumps(details, indent=4))
                self.details_text.insert(tk.END, "\n\n")
        else:
            self.details_text.insert(tk.END, "No matching anatomy found.")

    def display_anatomy_details(self, event=None):
        selected_anatomy = self.combobox.get()
        if not selected_anatomy:
            return

        details = anatomical_data.get(selected_anatomy, {})
        self.details_text.delete(1.0, tk.END)
        self.details_text.insert(tk.END, f"Anatomy: {selected_anatomy}\n")
        self.details_text.insert(tk.END, json.dumps(details, indent=4))

if __name__ == "__main__":
    root = tk.Tk()
    app = AnatomyApp(root)
    root.mainloop()
