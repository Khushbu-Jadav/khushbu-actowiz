from rich import print
import json
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="actowiz",
    database="swiggy_data"
)

cursor = conn.cursor()


with open(r"C:\python practice\day3\swiggy_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for item in data:
    single_data = (item.get("restaurentname", ""), item.get("itemname",""), item.get("image_url"), item.get("price"),
                   item.get("final_price"), item.get("discount"), item.get("ratings"), item.get("restaurent_avg_rating"),
                   item.get("isVag"), item.get("rating_count"), str(item.get("offers")), item.get("restuarent_url"), item.get("restaurent_address"))
    try:
        cursor.execute("""
                    INSERT INTO swiggy_restaurent_data(
                                restaurent_name,
                                itemname,
                                image_url,
                                price,
                                final_price,
                                discount,
                                ratings,
                                restaurent_avg_rating,
                                isVag,
                                rating_count,
                                offers,
                                restaurent_url,
                                restaurent_address)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, single_data)
        print(" Data inserted successfully!")
    except Exception as e:
        print(" Error inserting:", e)


conn.commit()
cursor.close()
conn.close()













