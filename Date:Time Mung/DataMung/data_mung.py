import pandas as pd

data_set = pd.read_csv("/Users/williamshelton/Desktop/PIXLEE_predictive_modeling/Date:Time Mung/Original Datasets/original_dataset.csv")

pieces = [data_set["instagram_likes"], data_set["instagram_followers"], data_set["created_at"], data_set["title"]]

new_df = pd.concat(pieces, axis=1)

new_df.to_csv("first_training_dataset.csv")