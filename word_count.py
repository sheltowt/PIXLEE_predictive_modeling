import pandas as pd
import collections

dataset = pd.read_csv("first_training_dataset.csv")

titles = dataset["title"]

wordArray = []

def wordCount(data_frame_column):
  for titleString in data_frame_column:
    titleString = str(titleString)
    titleString.replace("#", " #")
    words = titleString.split()
    for word in words:
      wordArray.append(word)
  counter = collections.Counter(wordArray)
  return counter.most_common(100)
    
top100hashtags = wordCount(titles)

arrayoftop100 = []

for x in top100hashtags:
  dataset[x[0]] = 0
  arrayoftop100.append(x[0])

def top100words(processed_dataset):
  count = -1
  titles = processed_dataset["title"]
  for x in titles:
    count += 1
    titleString = str(x)
    titleString.replace("#", " #")
    words = titleString.split()
    for word in words:
      if word in arrayoftop100:
        processed_dataset[word][count] = 1
        
top100words(dataset)      


dataset.to_csv("dataset_100mostcommonhashtags.csv")

