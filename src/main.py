import tkinter as tk
import tkinter.font as tkFont
import configparser


class Seed:
    def __init__(self, name, json):
        self.name = name
        self.json = json


def generate_seed(seed):
    print(seed.json)


def create_buttons(seeds: list[Seed]):
    num_buttons = len(seeds)
    num_cols = int(num_buttons**0.5)
    num_rows = (num_buttons + num_cols - 1) // num_cols
    custom_font = tkFont.Font(weight="bold", size=30)

    for i, seed in enumerate(seeds):
        row = i // num_cols
        col = i % num_cols
        button = tk.Button(root, text=seed.name, command=lambda loop_seed=seed: generate_seed(loop_seed), font=custom_font)
        button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

    exit_button = tk.Button(root, text="Exit", command=root.quit, font=custom_font)
    exit_button.grid(row=num_rows, columnspan=num_cols, padx=5, pady=5, sticky="nsew")

    return num_cols


def get_seeds():
    config = configparser.ConfigParser()
    config.read("config.ini")
    seeds = []
    for section in config.sections():
        seeds.append(Seed(config[section]["name"], config[section]["json"]))
    return seeds


def setup_grid(setup_root, setup_num_cols):
    for i in range(len(seeds) + 1):
        setup_root.grid_rowconfigure(i // setup_num_cols, weight=1)
        setup_root.grid_columnconfigure(i % setup_num_cols, weight=1)


root = tk.Tk()
root.geometry("1280x800")
root.title("Alttp-Rando Seed Generator")
seeds = get_seeds()
num_cols = create_buttons(seeds)
setup_grid(root, num_cols)

root.mainloop()
