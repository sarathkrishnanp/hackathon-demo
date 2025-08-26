import psycopg2

try:
    conn = psycopg2.connect(
        dbname="postgres",                    
        user="postgres",                      
        password="Sarath@2001",               
        host="db.sniepswimfrmonwiiski.supabase.co",  
        port="5432"
    )
    print("Connection successful!")
    conn.close()
except Exception as e:
    print("Connection failed!")
    print(e)
