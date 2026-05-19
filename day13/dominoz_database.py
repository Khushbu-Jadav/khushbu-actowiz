from rich import print
import json
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="actowiz",
    database="dominoz_db"
)

cursor = conn.cursor()

with open(r"C:\python practice\day13\dominoz_loc_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

    for d in data:
        single_data = (d.get("Pizza_name"), d.get("Restaurant_link"),d.get("image_link"),
                       d.get("city_name"),d.get("address"),d.get("pincode"),d.get("delivery_in"),
                       d.get("cost"),d.get("hours"),d.get("good_for"),d.get("phone_number"),d.get("view_menu"),
                       d.get("order_now"))

        try:
                    cursor.execute("""
                                INSERT INTO pizza_data(
                                    pizza_name,
                                    Restaurant_link,
                                    image_link,
                                    city_name,
                                    address,
                                    pincode,
                                    delivery_in,
                                    cost,
                                    hours,
                                    good_for,
                                    phone_number,
                                    view_menu,
                                    order_now
                                )
                        VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """, single_data)
                    print(" Data inserted successfully!")
        except Exception as e:
                    print(" Error inserting:", e)

conn.commit()
cursor.close()
conn.close()
