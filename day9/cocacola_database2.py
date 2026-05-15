import json
from rich import print
import jmespath
import mysql.connector

with open(r"C:\python practice\day9\coca_cola_instagram_data.json","r",encoding='utf-8') as f:
    data=json.load(f)

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="actowiz",
        database="cocacola_database"
    )

    try:
        cursor = conn.cursor()
        cursor.execute('CREATE DATABASE IF NOT EXISTS cocacola_database')

        try:
            cursor.execute('DROP TABLE IF EXISTS profile')
            cursor.execute('DROP TABLE IF EXISTS post')
            cursor.execute('DROP TABLE IF EXISTS related_profiles')


        except Exception as e:
            print("can't delete table")


        cursor.execute(
            """
                create table if not exists profile(
                profile_id bigint primary key not null,
                user_name varchar(255),
                full_name varchar(255),
                profile_image_url text,
                profile_url text,
                followers int,
                following int,
                biography varchar(255),
                total_post int
                )
            """)

        cursor.execute(
            """
                create table if not exists post(
                post_id bigint primary key not null,
                post_url text,
                post_likes int,
                post_comments int,
                post_image_display_url text,
                profile_id bigint,
                foreign key(profile_id) references profile(profile_id)
                )            
            """
        )

        cursor.execute(
            """
                create table if not exists related_profiles(
                related_profile_id bigint primary key not null,
                related_profile_username varchar(255),
                related_profile_fullname varchar(255),
                related_profile_pic_url text,
                related_profile_url text,
                profile_id bigint,
                foreign key(profile_id) references profile(profile_id)
                )
            """
        )

        cursor.execute("""
                    insert into profile(
                        profile_id,
                        user_name,
                        full_name,
                        profile_image_url,
                        profile_url,
                        followers,
                        following,
                        biography,
                        total_post
                    ) values (%s ,%s, %s, %s, %s, %s, %s, %s, %s)""",
                       (jmespath.search('profile_id', data),
                        jmespath.search('user_name', data),
                        jmespath.search('full_name', data),
                        jmespath.search('profile_image_url', data),
                        jmespath.search('profile_url', data),
                        jmespath.search('followers', data),
                        jmespath.search('following', data),
                        jmespath.search('biography', data),
                        jmespath.search('total_posts', data)
                        )
                )
        print("profile data inserted")

        for post in jmespath.search("post[*]",data):
            cursor.execute("""
                                insert into post(
                                    post_id,
                                    post_url,
                                    post_likes,
                                    post_comments,
                                    post_image_display_url,
                                    profile_id
                                ) values (%s ,%s, %s, %s, %s, %s)
                            """,
                           (jmespath.search('post_id', post),
                           jmespath.search('post_url', post),
                           jmespath.search('post_likes', post),
                           jmespath.search('post_comments', post),
                           jmespath.search('post_image_display_url', post),
                           jmespath.search('profile_id', data),
                           ))
            print("post data inserted successfully.")

        for related in jmespath.search("related_profiles[*]",data):
            cursor.execute("""
                           insert into related_profiles(
                               related_profile_id,
                               related_profile_username,
                               related_profile_fullname,
                               related_profile_pic_url,
                               related_profile_url)
                           values(%s,%s,%s,%s,%s)
                           """,
                           (
                           jmespath.search('related_profile_id', related),
                           jmespath.search('related_profile_username', related),
                           jmespath.search('related_profile_fullname', related),
                           jmespath.search('related_profile_pic_url', related),
                           jmespath.search('related_profile_url', related),
                           jmespath.search('profile_id', data)
                           ))
            print("related profile data inserted successfully.")

    except Exception as e:
        print(str(e))

conn.commit()
cursor.close()
conn.close()






