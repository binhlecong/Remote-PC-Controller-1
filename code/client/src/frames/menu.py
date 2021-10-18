import tkinter as tk
from PIL import Image, ImageTk
from tkinter import PhotoImage
import src.textstyles as style
import src.themecolors as THEMECOLOR


class Menu(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg=THEMECOLOR.body_bg, padx = 150, pady = 30)
        self.create_widgets()

    def create_icons(self):
        self.icons = {}
        self.icons['screen'] = self.create_sprite('assets/menu/ic_screen.png')
        self.icons['filesys'] = self.create_sprite('assets/menu/ic_filesystem.png')
        self.icons['registry'] = self.create_sprite('assets/menu/ic_registry.png')
        self.icons['app'] = self.create_sprite('assets/menu/ic_app.png')
        self.icons['process'] = self.create_sprite('assets/menu/ic_process.png')
        self.icons['keyboard'] = self.create_sprite('assets/menu/ic_keyboard.png')
        self.icons['shutdown'] = self.create_sprite('assets/menu/ic_shutdown.png')
        self.icons['logout'] = self.create_sprite('assets/menu/ic_logout.png')

    def create_sprite(self, path):
        image = Image.open(path)
        image.mode = 'RGBA'
        return ImageTk.PhotoImage(image)

    def create_widgets(self):
        # --------------------- Group 1 ---------------------
        # Take screenshot

        self.create_icons()

        self.btn_screen = tk.Button(
            self, text="Screen", image=self.icons['screen'], compound=tk.LEFT)
        self.btn_screen.grid(
            row=0, column=0, sticky=tk.W+tk.S+tk.E+tk.N, padx=20, pady=10, columnspan=3)
        self.btn_screen.config( height = 100, width = 300)
        # File system
        self.btn_filesys = tk.Button(
            self, text="File system", image=self.icons['filesys'], compound=tk.LEFT)
        self.btn_filesys.grid(
            row=1, column=0, sticky=tk.W+tk.S+tk.E+tk.N, padx=20, pady=10, columnspan=3)
        self.btn_filesys.config( height = 100, width = 100)
        # Change registry
        self.btn_registry = tk.Button(
            self, text="Registry", image=self.icons['registry'], compound=tk.LEFT)
        self.btn_registry.grid(
            row=2, column=0, sticky=tk.W+tk.S+tk.E+tk.N, padx=20, pady=10, columnspan=3)
        self.btn_registry.config( height = 100, width = 300)
        # --------------------- Group 2 ---------------------
        # Show running applications
        self.btn_app = tk.Button(
            self, text="Appications", image=self.icons['app'], compound=tk.LEFT)
        self.btn_app.grid(row=0, column=3, sticky=tk.N + tk.W, padx=30, pady=10, columnspan=3)
        self.btn_app.config( height = 100, width = 300)
        # Show running processes
        self.btn_process = tk.Button(
            self, text="Processes", image=self.icons['process'], compound=tk.LEFT)
        self.btn_process.grid(row=1, column=3, sticky=tk.N + tk.W, padx=30, pady=10, columnspan=3)
        self.btn_process.config( height = 100, width = 300)
        # Get keystroke
        self.btn_keyboard = tk.Button(
            self, text="Keyboard", image=self.icons['keyboard'], compound=tk.LEFT)
        self.btn_keyboard.grid(
            row=2, column=3, sticky=tk.N + tk.W, padx=30, pady=10, columnspan=3)
        self.btn_keyboard.config( height = 100, width = 300)
        # --------------------- Group 3 ---------------------
        # Shutdown computer
        self.btn_shutdown = tk.Button(
            self, text="Shut down", image=self.icons['shutdown'], compound=tk.LEFT)
        self.btn_shutdown.grid(
            row=3, column=0, sticky=tk.W + tk.E + tk.N, padx=10, pady=10, columnspan=2)
        self.btn_shutdown.config( height = 100, width = 200)
        # Logout computer
        self.btn_logout = tk.Button(
            self, text="Log out", image=self.icons['logout'], compound=tk.LEFT)
        self.btn_logout.grid(row=3, column=2, sticky=tk.W + tk.N, padx=10, pady=10, columnspan=2)
        self.btn_logout.config( height = 100, width = 200)
        # Exit program
        self.btn_quit = tk.Button(
            self, text="Quit program", fg="red", compound=tk.LEFT)
        self.btn_quit.grid(row=3, column=4, sticky= tk.N + tk.W + tk.E + tk.S, padx=10, pady=10, columnspan=2)