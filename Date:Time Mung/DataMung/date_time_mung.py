import pandas as pd
import datetime
import dateutil.parser

unmunged = pd.read_csv("/Users/williamshelton/Desktop/PIXLEE_predictive_modeling/Date:Time Mung/Datasets/time_hashtag_dataset.csv")

for x in unmunged["created_at"]:
  try:
    x = dateutil.parser.parse(x)
    z = datetime.date.timetuple(x)
    print z[6]
    print x.hour
  except:
    pass
