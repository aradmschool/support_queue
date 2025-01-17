import os
from supabase import create_client, Client
from data_generator import *  
from dotenv import load_dotenv

load_dotenv()

supabase: Client = create_client(os.getenv('SUPABASE_URL'), os.getenv('SUPABASE_KEY'))

tables = support_queue_data_generator(params)

for table in tables:
    try:
        dict_data = tables[table].to_dict(orient='records')
        response = supabase.table(table).insert(dict_data).execute()
        print(f"Data inserted into {table} table successfully!")
    except Exception as e:
        print(f"Error inserting data into {table} table: {e}")