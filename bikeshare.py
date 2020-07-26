import time
import pandas as pd
import numpy as np
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("What city would you like data form, Chicago, New York City, Washington)\n")
        if city not in CITY_DATA:
           print("Please choose from one of the following cities: Chicago, New York City, or Washington\n")
           continue
        else:
           break
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month_input = input("What month would you like to look at? For all months type 'all'\n")
        if month_input not in CITY_DATA:
            print("Specifically type months between January and June")
            continue
        else:
            break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day_input = input("What day would you like to look at? For all days of the week type 'all'\n")
        if day_input not in CITY_DATA:
            print("Type a day of the week. For all days, type 'all'.")
            continue
        else:
            break
    print('-'*40)
    return city, month, day
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    return df
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # TO DO: display the most common month
    df['month']= df['Start Time'].dt.month
    common_month = df['month'].mode()[0]
    print("The most popular month of travel was {}.\n".format(common_month))

    # TO DO: display the most common day of week
    df['day']= df['Start Time'].dt.weekday_name
    common_day = df['day'].mode()[0]
    print("The most popular day of travel was {}.\n".format(common_day))

    # TO DO: display the most common start hour
    df['hour']= df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print("The most common hour of travel is at {}.\n".format(common_hour))

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    print()
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['Start Station'].size().nlargest(1)
    print("The most popular start station was {}.\n".format(common_start))

    # TO DO: display most commonly used end station
    common_end = df['End Station'].size().nlargest(1)
    print("The most popular end station was {}.\n".format(common_end))

    # TO DO: display most frequent combination of start station and end station trip
    se_combined = df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    print("The most frequently used start to end stations combined was {}.\n".format(se_combined))
    print()
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print("The total travel time was {}.\n".format(total_travel))

    # TO DO: display mean travel time
    average_travel = df['Trip Duration'].mean()
    print("The average travel time per trip was {}.\n".format(average_travel))
    print()
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # TO DO: Display counts of user types
    if 'User Type' in df.columns:
        user_types = df['User Type'].value_counts()
        print("The user type counts are: {}\n".format(user_types))

    # TO DO: Display counts of gender
        gender_counts = df['Gender'].value_counts()
        print("The gender type counts are: {}\n".format(gender_counts))
    else:
        print("Sorry not unavailable!")

    # TO DO: Display earliest, most recent, and most common year of birth
    earliest = min(df['Birth Year'])
    most_recent = max(df['Birth Year'])
    most_common = df['Birth Year'].mode
    print("The earliest year of birth was {}.\n".format(earliest))
    print("The most recent year of birth was {}.\n".format(most_recent))
    print("The most common year of birth was {}.\n".format(most_common))
    #except:
    print("Sorry. Data unavailable!")
    print()
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
