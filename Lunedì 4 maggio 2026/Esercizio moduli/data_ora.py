from datetime import datetime


def ottieni_data_corrente():
    
    now = datetime.now()
    return now.strftime("%d/%m/%Y %H:%M")   # per formattare la data in modo leggibile