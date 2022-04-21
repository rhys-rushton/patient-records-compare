import pandas as pd

def data_processing(rhino_report, red_rc, DSPatients):

    start_date = input('Please input the date you would like to start from (Inlcusive)')
    end_date = input('Please input the date you would like to end at (Inlcusive)')
    rhino_report = pd.read_excel(rhino_report)
    print(rhino_report)


data_processing()


