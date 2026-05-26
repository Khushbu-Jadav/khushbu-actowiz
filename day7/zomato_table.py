from rich import print
import json
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="actowiz",
    database="zomato_data"
)

cursor = conn.cursor()

with open(r"C:\python practice\day7\zomato_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)[0]['menu_categories']

    for menu in data:
        for items in menu.get('category'):
            for item in items.get('items'):
                single_data = (items.get("name", ""), item.get("item_id ",""), item.get("item_name"), str(item.get("item_slugs")),
                            item.get("item_url"), item.get("item_description"), item.get("item_price"), item.get("is_Veg"))

                try:
                    cursor.execute("""
                                INSERT INTO zomato_menu_data(
                                            category_name,
                                            item_id,
                                            item_name,
                                            item_slugs,
                                            item_url,
                                            item_description,
                                            item_price,
                                            is_Veg
                                )
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                    """, single_data)
                    print(" Data inserted successfully!")
                except Exception as e:
                    print(" Error inserting:", e)

conn.commit()
cursor.close()
conn.close()