import json
import jmespath
from rich import print

# username,full name,image url,follower,following,like & comments count,reel url,suggest accounts,post,profile pic photo

with open("coca_cola_instagram.json","r",encoding="utf-8") as f:
    data=json.load(f)

    res_data=[]

    res_data.append({
        "profile_id":jmespath.search("data.user.id",data),
        "user_name":jmespath.search("data.user.username",data),
        "full_name":jmespath.search("data.user.full_name",data),
        "profile_image_url":jmespath.search("data.user.profile_pic_url",data),
        "profile_url":"https://www.instagram.com/"+jmespath.search("data.user.username",data),
        "followers":jmespath.search("data.user.edge_followed_by.count",data),
        "following":jmespath.search("data.user.edge_follow.count",data),
        "biography":jmespath.search("data.user.biography",data),
        "bio_links":[
            {
                "title":jmespath.search("title",bio),
                "url":jmespath.search("url",bio)
            }for bio in jmespath.search("data.user.bio_links[*]",data)
        ],
        "total_post":jmespath.search("data.user.edge_owner_to_timeline_media.count",data),
        "post":[
            {
                "post_id":jmespath.search("node.id",post),
                "post_url":"https://www.instagram.com/cocacola/p/"+jmespath.search("node.shortcode",post),
                "post_comment":jmespath.search("node.edge_media_to_comment.count",post),
                "post_likes":jmespath.search("node.edge_liked_by.count",post),
                "post_image_display_url":jmespath.search("node.display_url",post)
            }  for post in jmespath.search("data.user.edge_owner_to_timeline_media.edges[*]",data)
        ],
        "related_profiles":[
            {
                "related_profile_id":jmespath.search("node.id",related),
                "related_profile_username":jmespath.search("node.username",related),
                "related_profile_full_name":jmespath.search("node.full_name",related),
                "related_profile_pic_url":jmespath.search("node.profile_pic_url",related),
                "related_profile_url":"https://www.instagram.com/"+jmespath.search("node.username",related)
            } for related in jmespath.search("data.user.edge_related_profiles.edges[*]",data)
        ]

    })

print(res_data)

with open("coca_cola_instagram_data.json","w",encoding='utf-8') as f:
    json.dump(res_data,f,indent=4)