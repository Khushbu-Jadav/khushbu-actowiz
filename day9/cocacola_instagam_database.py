import json
from rich import print
import mysql.connector

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="actowiz",
    database="cocacola"
)

cursor=conn.cursor()

with open("coca_cola_instagram_data.json",'r',encoding='utf-8') as f:
    data=json.load(f)

# for item in data:
#     profile_data=(item.get("profile_id"),item.get("user_name"),item.get("full_name"),item.get("profile_image_url"),
#                  item.get("profile_url"),item.get("followers"),item.get("following"),item.get("biography"),item.get("total_post"))
#
#     try:
#         cursor.execute("""
#             insert into profile(
#                 id,
#                 user_name,
#                 full_name,
#                 profile_image_url,
#                 profile_url,
#                 followers,
#                 following,
#                 biography,
#                 total_post
#             ) values (%s ,%s, %s, %s, %s, %s, %s, %s, %s)
#         """,profile_data)
#
#     except Exception as e:
#         print(" Error inserting:", e)
#
# for item in data[0].get('post'):
#     post_data=(item.get("post_id"),item.get("post_url"),item.get("post_likes"),item.get("post_comments"),item.get("post_image_display_url"))
#
#     try:
#         cursor.execute("""
#                     insert into post(
#                         post_id,
#                         post_url,
#                         post_likes,
#                         post_comments,
#                         post_image_display_url
#                     ) values (%s ,%s, %s, %s, %s)
#                 """, post_data)
#         print("data inserted successfully.")
#
#     except Exception as e:
#         print(" Error inserting:", e)


    for item in data[0].get('related_profiles'):
        related_profile=(item.get("related_profile_id"),item.get("related_profile_username"),item.get("related_profile_full_name"),
                     item.get("related_profile_pic_url"),item.get("related_profile_url"))

        try:

            cursor.execute("""
                insert into related_profiles(
                    related_profile_id,
                    related_profile_username,
                    related_profile_fullname,
                    related_profile_pic_url,
                    related_profile_url)
                values(%s,%s,%s,%s,%s)
                """,related_profile)
            print("data inserted successfully.")

        except Exception as e:
            print(" Error inserting:", e)

conn.commit()
cursor.close()
conn.close()
