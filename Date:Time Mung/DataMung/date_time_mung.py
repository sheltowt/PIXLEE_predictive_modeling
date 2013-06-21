import pandas as pd
import datetime
import dateutil.parser

unmunged = pd.read_csv("/Users/williamshelton/Desktop/PIXLEE_predictive_modeling/Date:Time Mung/Datasets/time_hashtag_dataset.csv")

unmunged["day_week"] = 0

unmunged["hour_day"] = 0

count = -1
for x in unmunged["created_at"]:
  count += 1
  try:
    x = dateutil.parser.parse(x)
    z = datetime.date.timetuple(x)
    unmunged["day_week"][count] = z[6]
    unmunged["hour_day"][count] = x.hour
  except:
    pass

unmunged.to_csv("/Users/williamshelton/Desktop/PIXLEE_predictive_modeling/Date:Time Mung/Datasets/time_hashtag_MLdataset.csv")
