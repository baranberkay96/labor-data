from os import sep
import pandas as pd
from occupationcoder.coder import coder
import csv
from mq import Queue
custom_coder = coder.Coder()

if __name__ == '__main__':
    queue = Queue()

    filename = queue.rpop('files')

    print(filename)

    df = pd.read_csv(f'./parts_draft/{filename}', sep='|', error_bad_lines=False, quoting=csv.QUOTE_NONE, encoding='utf-8', header=None)
    df.columns = ['id', 'id_x', 'job_title', 
                    'source_id', 'job_sector', 'type', 'county',
                    'city', 'posted_by', 'publish_date', 'floor_wage',
                    'ceiling_wage', 'currency', 'job_description']

    df = custom_coder.codedataframe(df)
    
    df.to_csv(f'./parts/{filename}', sep='|', mode='a', quoting=csv.QUOTE_NONE)