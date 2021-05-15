from pymongo import MongoClient
import pandas as pd

# Connection to Mongo DB
client = MongoClient("mongodb+srv://abdielquintero:admin201@cluster0.r0nej.mongodb.net/test")
DB = client['Yapaya']


def QUOTATION_DF(columns: list = None):
    return pd.DataFrame(DB.cotizaciones.find(), columns=columns)


def APC_DF(columns: list = None):
    return pd.DataFrame(DB.apcs.find(), columns=columns)


def LOAN_DF(columns: list = None):
    return pd.DataFrame(DB.loans.find(), columns=columns)


def MOBILE_LOAN_DF(column: list = None):
    return pd.DataFrame(DB.mobile_loan_applications.find(), columns=column)


def PAYMENT_DF(columns: list = None):
    return pd.DataFrame(DB.payments.find(), columns=columns)


def CUSTOMER_DF(columns: list = None):
    return pd.DataFrame(DB.customers.find(), columns=columns)

    # *** End Dataframe Function *** #


# Export dataframe to CSV
def export_to_csv(dataframe, file_name: str):
    dataframe.to_csv('{}.csv'.format(file_name), index=False, header=True)
    return 'File Created'
