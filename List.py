from tkinter import *
import sqlite3

class List(Frame):
  def __init__(self, master):
    super().__init__(master)

    self.container1 = Frame(master)
    self.container1.grid(column=0, row=0, sticky=(N, S, E, W))

    self.list = Listbox(self.container1, width=70)
    self.list.grid(column=0, row=0, sticky=(N,E,S))
    self.s = Scrollbar(self.container1, orient=VERTICAL, command=self.list.yview)
    self.s.grid(column=1, row=0, sticky=(N,S))
    self.list['yscrollcommand'] = self.s.set

    self.conn = sqlite3.connect("base.db")
    self.cursor = self.conn.cursor()

    # try:
    self.cursor.execute("""
    SELECT * FROM contacts;
    """)
    try:
      for linha in self.cursor.fetchall():
        print(linha)
        self.list.insert(END, "{0:50} {1:12} {2:1}\n" .format(linha[1], linha[2], linha[3]))
    except:
      print("DB error.")

    self.conn.close()
