from rich import print
import json
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="actowiz",
    database="harrisfarm_db"
)

cursor = conn.cursor()

with open(r"C:\python practice\day12\new_harrisfarm.json", "r", encoding="utf-8") as f:
    data = json.load(f)

    for d in data:
        single_data = (d.get("category_name", ""), d.get("category_link",""))

        try:
                    cursor.execute("""
                                INSERT INTO categories(
                                            category_name,
                                            category_link
                                )
                        VALUES (%s, %s)
                    """, single_data)
                    print(" Data inserted successfully!")
        except Exception as e:
                    print(" Error inserting:", e)

conn.commit()
cursor.close()
conn.close()
