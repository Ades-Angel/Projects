import tkinter as tk
import time


class StopWatch(tk.Frame):
    ''' Imlements a stop watch frame widget. '''
    def __init__(self, parent=None, **kw):
        tk.Frame.__init__(self, parent, kw)
        self.start = 0.0
        self.elapsedtime = 0.0
        self.running = 0
        self.timestr = tk.StringVar()
        self.makeWidgets()

    def makeWidgets(self):
        ''' Make the time label. '''
        label = tk.Label(self, textvariable=self.timestr, bg='Black',
                         fg='White', font=('Courrier', 50, 'bold'))
        self.setTime(self.elapsedtime)
        label.pack(fill=tk.BOTH, expand=1, pady=0, padx=0)

    def update(self):
        ''' Update the label with elapsed time. '''
        self.elapsedtime = time.time() - self.start
        self.setTime(self.elapsedtime)
        

    def Stops(self):
        ''' Stops the stopwatch. '''
        if self.running:
            self.after_cancel(self.timer)
            self.elapsedtime = time.time() - self.start
            self.setTime(self.elapsedtime)
            self.running = 0

    def Resets(self):
        ''' Resets the stopwatch. '''
        self.start = time.time()
        self.elapsedtime = 0.0
        self.setTime(self.elapsedtime)


def main():
    root = tk.Tk()
    root.configure(bg='black')
    root.title("Stopwatch")
    root.geometry("900x500")
    sw = StopWatch(root)
    sw.place(x=150, y=50, width=600, height=200)

    tk.Button(root, text='Start', command=sw.Starts, bg='Black',
              fg='White', font=("Courrier", 20, "bold")).place(x=20, y=300,
                                                               width=200,
                                                               height=50)
    tk.Button(root, text='Stop', command=sw.Stops, bg='Black',
              fg='White', font=("Courrier", 20, "bold")).place(x=240, y=300,
                                                               width=200,
                                                               height=50)
    tk.Button(root, text='Clear', command=sw.Resets, bg='Black',
              fg='White', font=("Courrier", 20, "bold")).place(x=460, y=300,
                                                               width=200,
                                                               height=50)
    tk.Button(root, text='Quit', command=root.quit, bg='Black',
              fg='White', font=("Courrier", 20, "bold")).place(x=680, y=300,
                                                               width=200,
                                                               height=50)

    root.mainloop()


if __name__ == '__main__':
    main()
