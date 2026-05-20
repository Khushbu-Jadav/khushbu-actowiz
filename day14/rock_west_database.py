import json
from rich import print
import mysql.connector

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="actowiz",
    database="rock_west_db"
)

cur=conn.cursor()

with open(r"C:\python practice\day14\rock_west_scrap.json", "r", encoding="utf-8") as f:
    data = json.load(f)

    # for d in data:
    #     single_data=(d.get("product_name"),d.get("product_link"),d.get("product_sku"),
    #                 d.get("product_price"),d.get("product_quantity"),d.get("is_available"))
        
    #     try:
    #         cur.execute(
    #             """
    #                 insert into rock_west_data(
    #                 product_name,
    #                 product_link,
    #                 product_sku,
    #                 product_price,
    #                 product_quantity,
    #                 is_available
    #                 ) values (%s,%s,%s,%s,%s,%s)
    #             """,single_data
    #         )
    #         print("Data inserted successfully!")

    #     except Exception as e:
    #                 print(" Error inserting:", e)

    for d in data:
        info = d.get("product_additional_info")[0]
        second_data=(info.get("application"),info.get("materials"),info.get("pattern"),info.get("angle_corner_style"),
                    info.get("angle_degree"),info.get("angle_finish"),info.get("angle_leg_length"),info.get("angle_thickness"),info.get("thickness"),
                    info.get("length"),info.get("length(max_continous)"),info.get("max_operating_temp(tg)"),info.get("HTS - Harmonized Tariff Code"))
        try:
            cur.execute(
            """
            INSERT INTO additional_info(
                application,
                materials,
                pattern_,
                angle_corner_style,
                angle_degree,
                angle_finish,
                angle_leg_length,
                angle_thickness,
                thickness,
                length_,
                length_max_continous,
                max_operating_temp_tg,
                hts_harmonized_tariff_code
            ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """,
            second_data
        )
            print("Data inserted successfully!")

        except Exception as e:
                    print(" Error inserting:", e)

conn.commit()
cur.close()
conn.close()