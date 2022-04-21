from cgitb import text
from tkinter import *
from tkinter import ttk
import tkinter.filedialog
from tokenize import String
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
    	
        ttk.Label(mainframe, text = 'Please select the rhino report').grid(column=1, row=1, sticky=W)
        self.rhino_file = StringVar()
        ttk.Button(mainframe, text = 'Load Rhino File', command = lambda: self.get_location(self.rhino_file, 'Load Rhino')).grid(column=3,row=1, sticky=E)
        
        ttk.Label(mainframe, text = 'Please select the REDRC File').grid(column=1, row=2, sticky=W)
        self.red_rc = StringVar()
        ttk.Button(mainframe, text = 'Load REDRC File', command = lambda: self.get_location(self.red_rc, 'Load REDRC')).grid(column=3,row=2, sticky=E)
        
        
        ttk.Label(mainframe, text='Please select DSP File').grid(column=1,row = 3, sticky= W)
        self.dsp_file = StringVar()
        ttk.Button(mainframe, text='Load DSP File', command = lambda: self.get_location(self.dsp_file, 'Load DSP')).grid(column=3,row=3, sticky=E)


        ttk.Button(mainframe, text = 'Compare Data', command = lambda: data_processing(self.rhino_file.get(), self.red_rc.get(), self.dsp_file.get())).grid(column=3, row=4, sticky= E)



root = Tk()
Compare_Data(root)
root.mainloop()