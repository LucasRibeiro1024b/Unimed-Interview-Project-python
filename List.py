from tkinter import *
from Contact import Contact

class List(Frame):
  def __init__(self, master):
    super().__init__(master)

    self.container1 = Frame(master)
    self.container1.grid(column=0, row=0, sticky=(N, S, E, W))
    self.container1.columnconfigure(0, weight=2)
    self.container1.rowconfigure(0, weight=1)

    self.list = Listbox(self.container1, height=5)
    self.list.grid(column=0, row=0, sticky=(N,W,E,S))
    self.s = Scrollbar(self.container1, orient=VERTICAL, command=self.list.yview)
    self.s.grid(column=1, row=0, sticky=(N,S))
    self.list['yscrollcommand'] = self.s.set
    # self.label = Label(self.container1, text="Status message here", anchor=(W)).grid(column=0, columnspan=2, row=1, sticky=(W,E))

    for i in range(1,101):
        self.list.insert('end', 'Line %d of 100' % i)
