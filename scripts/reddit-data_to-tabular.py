import os
import json
import pandas as pd

data_path = os.path.join('D:/', 'data', 'reddit')
filename = "reddit_rdenmark_01032021-08032021.json"

with open(os.path.join(data_path, filename), 'r', encoding = 'utf-8') as f:
    posts = json.load(f)
    
posts_df = pd.DataFrame.from_records(posts)

posts_df_long = posts_df.explode('comments').reset_index(drop=True).add_prefix('post_')
posts_df_long = pd.merge(posts_df_long, pd.json_normalize(posts_df_long['post_comments']).add_prefix('comment_'), left_index=True, right_index=True)

outname = "reddit_rdenmark-comments_01032021-08032021_long.csv"
posts_df_long.to_csv(os.path.join(data_path, outname), index = False)