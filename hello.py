from cgitb import text
from tkinter import *
from tkinter import ttk
import tkinter.filedialog
from pip import main
from data import data_processing

class Compare_Data:

    def get_location(self,file, file_name):
        #tkinter.filedialog.askopenfilename(parent=root, title='Please select file')
        file.set(tkinter.filedialog.askopenfilename(parent=root, title=f'Please {file_name} File'))
        print(file.get())
     
        

    def __init__(self, root):
        root.title('Data Comparison')

        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
    	
        self.file_one = StringVar()
        ttk.Button(mainframe, text = 'Load Rhino File', command = lambda: self.get_location(self.file_one, 'Load Rhino')).grid(column=3,row=1, sticky=E)
        
        self.file_two = ttk.Button(mainframe, text = 'Load File', command = self.get_location).grid(column=3,row=2, sticky=E)
        label_file_one = ttk.Label(mainframe, text = 'Please select the rhino report').grid(column=1, row=1, sticky=W)

        ttk.Button(mainframe, text = 'Compare Data', command = lambda: data_processing(self.file_one.get())).grid(column=3, row=3, sticky= E)



root = Tk()
Compare_Data(root)
root.mainloop()