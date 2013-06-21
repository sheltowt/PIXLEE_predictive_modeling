PIXLEE_predictive_modeling
==========================

The purpose of this repo was to explore a strategy PIXLEE could implement to predict the virality of a photo, with the purpose of being able to select photos for a photo dashboard that had a high probability of virality.  The dataset I used was pulled from PIXLEE's API and contained information about Instagram photos that contained the #coke or #coca-cola hashtags. The three objectives of this project were to develop scripts that transformed the data into a format suitable for machine learning, to evaluate the amount of variance features contributed to the number of instagram_likes a photo recieved, and to evaluate how effective a variety of regression algorithms were at building a model to predict the number of likes a photo received.  

PIXLEE enables clients to collect, display and measure authentic user-generated photos.  Customers can leverage these photos to drive traffic and increase sales through interactive photo dashboards, or competitions.  

Data Munging-
Relevant features that could be pulled from the API included the number of followers of the poster, the hour and day of the week at which the photo was created, the title and hashtags associated with the photo, and the geographic location of the poster.  I extracted the day of the week, and hour of the day using pythons date time and dateutil packages.  The hashtag and title features I turned into a bag-of-words type feature.  I did this by adding fifty columns to the data set that matched the 50 most common hashtags or title words.  If the photos title contained that word the column had a 1, if not a 0.  

Variance Attribution Analysis-
The variance attributed to each feature in the model was similar to what I expected.  The number of followers a user had, as well as the hashtags a user used were significant indicators of the number of likes a photo would receive.  Also the number of comments a photo had, and the time of day and day of week the photo was taken contributed as well.  A break down of variance for a variety of feature combos is provided in the VarianceAnalysis folder.  

Predictive Modeling-
The dependent variable for this model was the number of likes a photo would recieve.  This variable was continuous and numeric so I used a variety of regression algorithms including decision trees, random forests, linear regression and neural nets.  The most effective algorithm evaluated was a random forest algorithm.  This algorithm produced a MSE of 2476 compared to 6530 if each photo was scored with the average number of likes.  

Next Steps-
Acquire a larger dataset-  features such as day of week and time of day would have yielded higher predicitive value if I had used a larger data set.  The data set I used only had three days worth of data.
Add photo computer vision clustering analysis as an additional feature- this would likely yeild significant performance improvements.
Scale algorithm with Python- the R package I was using only allowed for 32 categorical variables.  This prevented me from using geographic data due to the number of categories.




