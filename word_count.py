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
      word = word.lower()
      wordArray.append(word)
  counter = collections.Counter(wordArray)
  return counter.most_common(50)
    
top50hashtags = wordCount(titles)

arrayoftop50 = []

word_count = 0
for x in top50hashtags:
  dataset[x[0]] = 0
  arrayoftop50.append(x[0])
  word_count += 1

def top50words(processed_dataset):
  count = -1
  titles = processed_dataset["title"]
  for x in titles:
    count += 1
    titleString = str(x)
    titleString.replace("#", " #")
    words = titleString.split()
    word_count = 0
    for word in words:
      word = word.lower()
      if word in arrayoftop50:
        processed_dataset[word][count] = 1
      word_count += 1
        
top50words(dataset)      


dataset.to_csv("dataset_50mostcommonhashtags_error.csv")

