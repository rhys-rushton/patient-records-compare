# Patient Records Comparison

This is a tkinter app to compare various patient records to look for discrepencies amongst their covid testing records. 

The script uses the pandas library for analysing the excel spreadsheet and then uses tkinter for the GUI. 

The user inputs various csv files into the app and the app will output a result .xlsx file for the user. 

(app.JPG)


# Instructions for Creating an Executable 
pyinstaller --onefile -w -n "Compare Patients" --icon=icon.ico main.py

The above assumes you are using the pyinstaller package to bundle the script. 





