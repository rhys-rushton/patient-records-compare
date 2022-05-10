from tkinter import *
from tkinter import ttk
import tkinter.filedialog
from data import data_processing


class Compare_Data:

    def get_location(self,file, file_name, mainframe, col, row, sticky):
        #tkinter.filedialog.askopenfilename(parent=root, title='Please select file')
        file.set(tkinter.filedialog.askopenfilename(parent=root, title=f'Please Load {file_name} File'))
        if  file.get():
            Label(mainframe, text = f'{file_name} report uploaded').grid(column= col + 1, row= row, sticky= sticky)
        #print(file.get())

    def get_output_location(self, file):
        file.set(tkinter.filedialog.askdirectory(parent=root, title='Please Choose Where Output Goes'))
        #print(file.get())

  

    def get_data(self):
        res = data_processing(self.rhino_file.get(), self.red_rc.get(), self.dsp_file.get(), self.start_date.get(), self.end_date.get(), self.output_location.get())
        #self.change_label()
        if res == False:
            self.status_label['text'] = 'Error please make sure your inputs were correct, otherwise contact support'
        
        else:
            self.status_label['text'] = 'Process Complete'

        root.update()
        return

    def run_data(self, mainframe):
        status = StringVar(value='Currently Running Process. Please do not touch')
        self.status_label = ttk.Label(mainframe, text = status.get())
        self.status_label.grid(column=1, row = 8)
        root.update()
        self.get_data()
    
    

    def __init__(self, root):
        root.title('Data Comparison')
        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)	
        ttk.Label(mainframe, text = 'Please select the rhino report').grid(column=1, row=1, sticky=W)
        self.rhino_file = StringVar()
        ttk.Button(mainframe, text = 'Load Rhino File', command = lambda: self.get_location(self.rhino_file, 'Rhino', mainframe, 4, 1, E)).grid(column=3,row=1, sticky=E)  
        ttk.Label(mainframe, text = 'Please select the REDRC File').grid(column=1, row=2, sticky=W)
        self.red_rc = StringVar()
        ttk.Button(mainframe, text = 'Load REDRC File', command = lambda: self.get_location(self.red_rc, 'REDRC', mainframe, 4, 2, E)).grid(column=3,row=2, sticky=E)
        ttk.Label(mainframe, text='Please select DSP File').grid(column=1,row = 3, sticky= W)
        self.dsp_file = StringVar()
        ttk.Button(mainframe, text='Load DSP File', command = lambda: self.get_location(self.dsp_file, 'DSP',mainframe,  4, 3, E)).grid(column=3,row=3, sticky=E)
        ttk.Button(mainframe, text = 'Compare Data', command = lambda: self.run_data(mainframe)).grid(column=4, row=7, sticky= E)

        self.start_date = StringVar()
        entry_start_date = ttk.Entry(mainframe, textvariable=self.start_date)
        entry_start_date.grid(column=1, row = 4)
        entry_start_date.insert(END, 'Start Date: dd/mm/YYYY')
        ttk.Label(mainframe, text = 'Enter Start Date').grid(column=2, row=4)
        
        self.end_date = StringVar()
        entry_end_date = ttk.Entry(mainframe, textvariable=self.end_date)
        entry_end_date.grid(column=1, row=5)
        entry_end_date.insert(END, 'End Date: dd/mm/YYYY')
        ttk.Label(mainframe, text = 'Enter End Date').grid(column=2, row=5)

        self.output_location = StringVar()
        ttk.Button(mainframe, text='Choose Output Location', command= lambda: self.get_output_location(self.output_location)).grid(column=0,row=7)

        for child in mainframe.winfo_children(): 
            child.grid_configure(padx=5, pady=5)


root = Tk()
Compare_Data(root)
root.mainloop()