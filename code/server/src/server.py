import os
import socket
import tkinter as tk
from src.screenshot import Screenshot
from src.process import Process
from src.application import Application
from src.keystroke import KeyLogger


class Server:
    def __init__(self):
        super().__init__()
        self._root = tk.Tk()
        self._root.geometry('300x200')
        self._root.title("Server")
        self._root.btn_open_server = tk.Button(self._root, text = "OPEN SERVER", 
                                        font = ("Consolas 20 bold"), command = self.open_server)
        
        self._root.btn_open_server.place(relx = 0.5, rely = 0.5, anchor = tk.CENTER)


    def run(self):
        self._root.mainloop()

    def open_server(self):
        IP = (socket.gethostbyname('localhost'), 54321)
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(IP)
        self.server.listen(1)
        # ahihi do ngok
        #
        self.client, addr = self.server.accept()
        print("Connected by", addr)
        
        while True:
            cmd = self.client.recv(32).decode('utf8')
            if cmd == 'keystroke':
                self.keystroke()
            elif cmd == 'shutdown':
                self.shutdown()
            elif cmd == 'registry':
                self.registry()
            elif cmd == 'screenshot':
                self.screenshot()
            elif cmd == 'process':
                self.process()
            elif cmd == 'application':
                self.application()
            elif cmd == 'quit':
                break

        self.client.shutdown(socket.SHUT_RDWR)
        self.client.close()
        self.server.close()


    def keystroke(self):
        doit = KeyLogger(self.client)
        doit.run()
        pass

    def shutdown(self):
        os.popen("shutdown -s")
        pass

    def registry(self):
        pass

    def screenshot(self):
        doit = Screenshot(self.client)
        doit.run()
        pass

    def process(self):
        doit = Process(self.client)
        doit.run()
        pass

    def application(self):
        doit = Application(self.client)
        doit.run()
        pass

    pass