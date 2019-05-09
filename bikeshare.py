import time
import pandas as pd
import numpy as np
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


print('Hello! Let\'s explore some US bikeshare data!')
#Asking the user to choose the city when unexpected result, there is a loop
while True:
    city = input('Please choose the city: chicago, new york city or washington:\n ').lower()
    if city in ['chicago', 'new york city', 'washington']:
        break
    else: print('There must be an error, as {} is not accepted\n'.format(city))
print('you have choosen {}'.format(city))
#Asking the user to choose the filter month, day or none
while True:
    filter = input('Would you like to filter the data by month, day, or none?\n').lower()
    if filter in ['month', 'day', 'none']:
        break
    else: print('please rewrite correctly\n')
print('you have chosen to filter by {}'.format(filter))
#when the user choose none month and day are considered 'all'
if filter == 'none':
    month = 'all'
    day = 'all'
#when the user choose month, 'day' is considered as all and the user is asked to choose the month if not there is a loop
if filter == 'month':
    day = 'all'
    while True:
        month = input('Which month - january,february, march, april, may, or june?\n').lower()
        if month in ['january','february', 'march', 'april','may','june']:
            break
        else: print('{} is not correct, please choose the correct month\n'.format(month))
    print('you have chosen {}'.format(month))
#when the user choose the day, we considered all months and he must write the correct name of the day
if filter == 'day':
    month = 'all'
    while True:
        day = input('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?\n')
        if day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']:
            break
        else: print('{} is not correct, please write namely the day\n'.format(day))
    print('you have chosen {}'.format(day))
print('-'*40)
#calculation of the most frequent travel using the documentation in the course and in Panda online documentation
print('\nCalculating The Most Frequent Times of Travel...\n')
start_time = time.time()
df = pd.read_csv(CITY_DATA[city])
df['Start Time'] = pd.to_datetime(df['Start Time'])
df['month'] = df['Start Time'].dt.month
df['day_of_week'] = df['Start Time'].dt.weekday_name
if month != 'all':
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    month = months.index(month) + 1
    df = df[df['month'] == month]

if day != 'all':
    df = df[df['day_of_week'] == day.title()]

df['hour'] = df['Start Time'].dt.hour
#calculating the popular month, day and hour which was inlcuded in exercise
popular_month = df['month'].mode()[0]
popular_day_of_week=df['day_of_week'].mode()[0]
popular_hour = df['hour'].mode()[0]
print('Most Popular Month:', popular_month)
print("\nThis took %s seconds." % (time.time() - start_time))
print('-'*40)
print('Most Popular Day of the Week:', popular_day_of_week)
print("\nThis took %s seconds." % (time.time() - start_time))
print('-'*40)
print('Most Popular Start Hour:', popular_hour)
print("\nThis took %s seconds." % (time.time() - start_time))
print('-'*40)
#calculating the most popular Stations and trip
print('\nCalculating the Most Popular Stations and Trip')
start_time = time.time()
popular_station1 = df['Start Station'].mode()[0]
print('Most popular Start Station:', popular_station1)
print("\nThis took %s seconds." % (time.time() - start_time))
popular_station2 = df['End Station'].mode()[0]
print('Most popular End Station:', popular_station2)
print("\nThis took %s seconds." % (time.time() - start_time))
#this was the most difficult part to complete, I found that we can combine two row in one and then use mode
df['combined stations']= df['Start Station'] + df['End Station']
popular_station3 = df['combined stations'].mode()[0]
print ('most frequent combination of start station and end station trip:\n {}'.format(popular_station3))
print("\nThis took %s seconds." % (time.time() - start_time))
print('-'*40)
print('\nCalculating Trip Duration...\n')
start_time = time.time()
total_travel_time = df['Trip Duration'].sum()
print('Total travel time for {} is {}\n'.format(city, total_travel_time))
print("\nThis took %s seconds." % (time.time() - start_time))
print('-'*40)
mean_travel_time = df['Trip Duration'].mean()
print('Mean travel time for {} is {}\n'.format(city, mean_travel_time))
print("\nThis took %s seconds." % (time.time() - start_time))
print('-'*40)
#calcultion of User Stats
print('\nCalculating User Stats...\n')
start_time = time.time()
count_type = df['User Type'].value_counts()
print('The number of user by types is as fellow:\n', count_type)
if city == 'washington':
    print('there are no age and gender based data for washington')
else:
    gender_count = df['Gender'].value_counts()
    print('The distribution of customers by gender is as such\n', gender_count)
    earliest_birth = df['Birth Year'].min()
    recent_birth = df['Birth Year'].max()
    commonbirth =df['Birth Year'].mode()[0]
    print('the earliest year of birth is {}, the most recent is {} and the common year is {}\n'.format(earliest_birth, recent_birth, commonbirth))

print("\nThis took %s seconds." % (time.time() - start_time))
print('-'*40)
while True:
    see_data = input('do you want to see the first individual data? y or n \n').lower()
    if see_data in ['y', 'n']:
        break
    else: print('Error please write again y or n')
print(df.iloc[0:5])
i=0
while True:
    printmore = input('do you want to see more?\n').lower()
    if printmore == 'n':
        break
    else:
        i += 5
        print(df.iloc[i:i+5])
print ('Thanks, it is now completed!')
