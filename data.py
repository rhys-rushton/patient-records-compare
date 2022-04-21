import pandas as pd

def data_processing(rhino_report, red_rc, DSPatients):


    rhino_report = pd.read_excel(rhino_report)
    red_rc = pd.read_csv(red_rc, header=0, encoding='CP1252')
    DSPatients = pd.read_csv(DSPatients, header=0, encoding='CP1252')

    print('done')






