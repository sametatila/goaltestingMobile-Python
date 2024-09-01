from sqlalchemy import create_engine,text, Column, Integer, String, Date, Float
from sqlalchemy.orm import declarative_base
from database_models.database_url import DATABASE_URL

# Create the database engine
engine = create_engine(DATABASE_URL)

with engine.connect() as connection:
    # Uyku modundaki bağlantılar hakkında detaylı bilgi alma
    result = connection.execute(text("""
        SELECT 
            id, 
            user, 
            host, 
            db, 
            command, 
            time, 
            state, 
            info 
        FROM 
            information_schema.processlist 
        WHERE 
            Command = 'Sleep';
    """))
    sleep_connections = result.fetchall()

    kapat = 0

    # Uyku modundaki bağlantıları ve detaylarını listeleme
    for row in sleep_connections:
        if row['db'] == 'goaltest_gto_deneme':
            print(f"ID: {row['id']}, Kullanıcı: {row['user']}, Host: {row['host']}, Veritabanı: {row['db']}, Süre: {row['time']}, Durum: {row['state']}, Sorgu: {row['info']}")
            # Bağlantıyı kapatma
            if kapat == 1:
                connection.execute(text(f"KILL {row['id']};"))
        else:
            print(f"ID: {row['id']}, Kullanıcı: {row['user']}, Host: {row['host']}, Veritabanı: {row['db']}, Süre: {row['time']}, Durum: {row['state']}, Sorgu: {row['info']}")
# Bağlantıyı kapat
engine.dispose()