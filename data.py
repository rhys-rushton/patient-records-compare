import pandas as pd
from datetime import datetime

def data_processing(rhino_report, red_rc, dsp_patients, start_date, end_date, output_location):
    pd.set_option('display.float_format', lambda x: '%.0f' % x)
    fields_for_rhino = ['clinician_first_name', 'clinician_last_name', 'encounter_date', 'encounter_time', 'encounter_id', 'first_name', 'last_name', 'date_of_birth', 'age_at_presentation', 'gender', 'medicare_number', 'indigenous_status', 'address_line1', 'suburb', 'state', 'postcode', 'emergency_contact_name', 'country_of_birth','home_language', 'patient_symptoms', 'usual_medications', 'specimen_collected', 'diagnosis', 'outcome']
    rhino_report = pd.read_excel(rhino_report, dtype={'medicare_number': 'str'},usecols= fields_for_rhino)
    red_rc = pd.read_csv(red_rc, header=0, encoding='CP1252')
    dsp_patients = pd.read_csv(dsp_patients, header=0, encoding='CP1252')
    red_rc = red_rc.drop(columns=['Patient','Patient Type','Payer','Account Payer Type', 'Date','Brn','Doc','Stf','Inv #','Item','Transaction Type','Transaction Status','GST','Amount','Fee Type','Analysis Group'])
    red_rc = red_rc.rename(columns={'File #': 'FILE_NUMBER'})
    dsp_patients = dsp_patients.drop(columns=['patient_name','full_name', 'full_suburb', 'address', 'full_mailing_suburb', 'TITLE', 'HOME_ADDRESS_LINE_2', 'USUAL_CLINIC', 'USUAL_DOCTOR', 'TYPE_CODE',	'STATUS_CODE', 'PRACTICE_DEFINABLE_FIELD1_CODE', 'PRACTICE_DEFINABLE_FIELD2_CODE','PRACTICE_DEFINABLE_FIELD3_CODE',	'PRACTICE_DEFINABLE_FIELD4_CODE','PRACTICE_DEFINABLE_FIELD5_CODE','PRACTICE_DEFINABLE_FIELD6','PRACTICE_DEFINABLE_FIELD7',	'PRACTICE_DEFINABLE_FIELD8', 'PRACTICE_DEFINABLE_FIELD9', 'PRACTICE_DEFINABLE_FIELD10', 'FIRST_IN', 'LAST_IN', 'ALERTS', 'CLINIC_CODE', 'PATIENT_ID', 'MAILING_ADDRESS_LINE_1', 'MAILING_ADDRESS_LINE_2', 'MAILING_SUBURB_TOWN', 'MAILING_POSTCODE','FAMILY_ID' , 'email_ADDRESS', 'VETERAN_AFFAIRS_NUMBER','VETERAN_FILE_NUMBER_EXPIRY_DATE',	'PATIENT_HEALTH_CARE_CARD', 'PATIENT_HLTH_CARE_CARD_EX_DATE', 'SAFETY_NET_NO'])
    dsp_patients.FILE_NUMBER = dsp_patients.FILE_NUMBER.fillna(-1)
    dsp_patients.FILE_NUMBER = dsp_patients.FILE_NUMBER.astype(int)
    
    merged_data = pd.merge(red_rc, dsp_patients, on='FILE_NUMBER', how ='inner')
    #drop any duplicates made in the merge based off FILE_NUMBER and ENCOUNTER_DATE
    merged_data = merged_data.drop_duplicates(subset=['FILE_NUMBER', 'ServDate'])
    #format the data in the dataframe so the program can use it properly.
    # I want to have empty fields in a standard format that I can send to the browser. 
    merged_data = merged_data.fillna('')
    # I want to have the medicare number/ postocode as a string so I can slice easily and send to the browser. 
    merged_data.MEDICARE_NUMBER = merged_data.MEDICARE_NUMBER.astype(str)
    
    #print(merged_data_pcr)
    # remove whitepace in strings so I can index properly. 
    rhino_report['medicare_number'] = rhino_report['medicare_number'].str.replace(' ', '')
    merged_data['MEDICARE_NUMBER'] = merged_data['MEDICARE_NUMBER'].str.slice(start = 0, stop = 10)
    #merged_data['MEDICARE_NUMBER'] = merged_data['MEDICARE_NUMBER'].str.replace(' ', '')
    #merged_data['DATE_OF_BIRTH'] = merged_data['DATE_OF_BIRTH'].str.replace(' ', '')
    #rhino_report['date_of_birth'] = rhino_report['date_of_birth'].str.replace(' ', '')
    rhino_report['encounter_date'] = pd.to_datetime(rhino_report['encounter_date'], format='%d/%m/%Y')
    merged_data['ServDate'] = pd.to_datetime(merged_data['ServDate'], format='%d/%m/%Y')
    merged_data['DATE_OF_BIRTH'] = pd.to_datetime(merged_data['DATE_OF_BIRTH'], format='%d/%m/%Y')
    #merged_data['ServDate'] = merged_data['ServDate'].dt.strftime('%d/%m/%Y')
    #rhino_report['encounter_date'] = rhino_report['encounter_date'].dt.strftime('%d/%m/%Y')
    #rhino_report['encounter_date'] = rhino_report['encounter_date'].str.replace(' ', '')
    #merged_data['ServDate'] = merged_data['ServDate'].str.replace(' ', '')
    #rhino_report['date_of_birth'] = rhino_report['date_of_birth'].str.slice(start = 0, stop = 10)
    rhino_report['date_of_birth'] = pd.to_datetime(rhino_report['date_of_birth'], errors='coerce')
    rhino_report['date_of_birth'] = rhino_report['date_of_birth'].dt.date
    merged_data['DATE_OF_BIRTH']= merged_data['DATE_OF_BIRTH'].dt.date

    start_date = datetime.strptime(start_date, '%d/%m/%Y')
    end_date = datetime.strptime(end_date, '%d/%m/%Y')

    rhino_report_date_filter = rhino_report[(rhino_report.encounter_date >= start_date) & (rhino_report.encounter_date <= end_date)]
    merged_data_date_filter = merged_data[(merged_data.ServDate >= start_date) & (merged_data.ServDate <= end_date)]

    merged_data_date_filter = merged_data_date_filter.rename(columns = {'ServDate':'encounter_date', 'DATE_OF_BIRTH':'date_of_birth','MEDICARE_NUMBER': 'medicare_number'})


    indicator_values = {"left_only": "In Rhino", "right_only": "In REDRC", "both": "In Both reports"}
    new_df = rhino_report_date_filter.merge(merged_data_date_filter, on=['encounter_date','date_of_birth','medicare_number'] ,how='outer', indicator = True)
    new_df['_merge'] = new_df['_merge'].map(indicator_values)
    new_df.rename(columns= {'_merge':'Spreadsheet Location'}, inplace = True)
    #new_df = new_df.drop_duplicates(['encounter_date','date_of_birth','medicare_number'], keep='first')

    new_df = new_df.to_csv(f'{output_location}/comparison_output.csv', header = True)
    #rhino_report.to_csv('rhino.csv' , header = True)
    #merged_data.to_csv('test.csv', header=True)

    



 






