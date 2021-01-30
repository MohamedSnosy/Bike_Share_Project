import time
import pandas as pd
import numpy as np

CITY_DATA = { '1': 'chicago.csv',
              '2': 'new_york_city.csv',
              '3': 'washington.csv' }


def get_filters():
   
    
    """
    Asks user to specify a city, month, and day to analyze.
    
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('\nHello! Let\'s explore some US bikeshare data!')
    
   


    while True:
      city = input("\nchoose city would you like to filter by?\n 1 FOr Chicago\n 2 for  New York City\n  3 for Washington?\n")
      if city not in ('1', '2', '3'):
        print("please enter valid number")
        continue
      else:
        break
   
   

    while True:
      month_num = input("\nchoose month would you like to filter by?\n 1 for  January\n 2 for  February\n 3 for March\n 4 for April\n 5 for May\n 6 for June\n 7 for all")
      if month_num not in ('1', '2', '3', '4', '5', '6', '7'):
        print("please enter valid number")
        continue
      else:
        break
    if month_num == "1":
        month="January"
    elif month_num == "2":
        month = "February"
    elif month_num=="3":
        month ="March"
    elif month_num == "4":
        month="April"
    elif month_num == "5":
        month = "May"
    elif month_num=="6":
        month ="June"
    elif month_num == "7":
        month="all"
   

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
      day_num = input("\nchoose day? : 1 for  Sunday\n 2 for  Monday\n  3 for Tuesday\n 4 for Wednesday\n  5 for Thursday\n 6 for Friday\n 7 for Saturday\n 8 for all ")
      if day_num not in ('1', '2', '3', '4', '5', '6', '7', '8'):
        print("please enter valid number")
        continue
      else:
        break
        
    if day_num == "1":
        day="Sunday"
    elif day_num == "2":
        day = "Monday"
    elif day_num=="3":
        day ="Tuesday"
    elif day_num == "4":
        day="Wednesday"
    elif day_num == "5":
        day = "Thursday"
    elif day_num=="6":
        day ="Friday"
    elif day_num == "7":
        day="Saturday"
    elif day_num == "8":
        day="all"
    print('-'*40)
    return city, month, day


def load_data(city, month, day):

  
    df = pd.read_csv(CITY_DATA[city])


    df['Start Time'] = pd.to_datetime(df['Start Time'])


    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    if month != 'all':
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):

    print('\nloading\n')
    start_time = time.time()


    popular_month = df['month'].mode()[0]
    print(' Common Month:', popular_month)


    popular_day = df['day_of_week'].mode()[0]
    print(' Common day:', popular_day)



    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print(' Common Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):

    print('\nloading The Most Popular Stations and Trip...\n')
    start_time = time.time()

    Start_Station = df['Start Station'].value_counts().idxmax()
    print(' Commonly used start station:', Start_Station)



    End_Station = df['End Station'].value_counts().idxmax()
    print('\n Commonly used end station:', End_Station)



    Combination_Station = df.groupby(['Start Station', 'End Station']).count()
    print('\n Common  start station and end station trip:', Start_Station, " & ", End_Station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
  
    Total_Travel_Time = sum(df['Trip Duration'])
    print('Total travel time:', Total_Travel_Time/86400, " Days")

    Mean_Travel_Time = df['Trip Duration'].mean()
    print('Mean travel time:', Mean_Travel_Time/60, " Minutes")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
   

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    user_types = df['User Type'].value_counts()
    
    print('User Types:\n', user_types)


    try:
      gender_types = df['Gender'].value_counts()
      print('\nGender Types:\n', gender_types)
    except KeyError:
      print("\nGender Types:\nNo data  for this month.")

    try:
      Earliest_Year = df['Birth Year'].min()
      print('\nEarliest Year:', Earliest_Year)
    except KeyError:
      print("\nEarliest Year:\nNo data  for this month.")

    try:
      Most_Recent_Year = df['Birth Year'].max()
      print('\nMost Recent Year:', Most_Recent_Year)
    except KeyError:
      print("\nMost Recent Year:\nNo data  for this month.")

    try:
      Most_Common_Year = df['Birth Year'].value_counts().idxmax()
      print('\nMost Common Year:', Most_Common_Year)
    except KeyError:
      print("\nMost Common Year:\nNo data  for this month.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data(df):
    U_R = ''
   
    counter= 0
    while U_R not in['yes', 'no']:
          
        U_R = input("\nDo you want to view the raw data?:\n yes\n or no").lower()
     
        if U_R == "yes":
            print(df.head())
        elif U_R not in ['yes', 'no']:
            print("Input does not seem to match any of the accepted responses.")
        elif U_R != "yes":
            break

    
    while U_R == 'yes':
        print("Do you wish to view more raw data?")
        counter += 5
        U_R = input().lower()
        if U_R == "yes":
            print(df[counter:counter+5])
        elif U_R != "yes":
            break

    
        
        


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        display_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
            
if __name__ == "__main__":
    main()