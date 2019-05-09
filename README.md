### Date created
 Tue May 7 22:30:41 2019 +0000

### Project Title
Bikeshare project

### Description
The project is written in Python language and aims at retrieving from three cities Bikeshare database information asked by the users.
the code is based on Panda and Numpy libraries and make use of loop, inputs and conditional statements.
The first step was to define the city by asking the user between three cities.  loop verify the spelling and won't break until the intended one is given.
When this first condition is realized, the code asks if the data should be filtered by day, month or none. If unexpected answer is given, the user stay in a loop. Then if none is chosen, the code resume and print the code calculate the most popular month, day, start hour, stations, and trip duration. Otherwise, the user will be asked to provide the day or the month and the data will be filtered accordingly.
Then if Washington is chosen, the code print that there are no gender and age data. Otherwise, it gives the data per age and gender. Then the code asks user if they want to display individual data. When it has displayed, there is a loop that will ask to display the next information until the user answer no.

### Files used
bikeshare.py, chicago.csv, new_york_city.csv, Washington.csv

### Credits
Udacity's Nanodegree Programming for Data Science.
