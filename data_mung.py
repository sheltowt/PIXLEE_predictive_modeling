import pandas as pd

data_set = pd.read_csv("coke_api613_100k.csv")

pieces = [data_set["instagram_likes"], data_set["instagram_comments"], data_set["instagram_followers"], data_set["country"], data_set["title"],data_set["zip"]]

new_df = pd.concat(pieces, axis=1)

print new_df